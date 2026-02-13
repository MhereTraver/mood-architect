from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
import random  
import time


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Mood Architect API",
    description="Generate personalized therapeutic affirmations",
    version="1.0.0"
)

# Configure CORS
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://*.vercel.app",
]

FRONTEND_URL = os.getenv("FRONTEND_URL", "")
if FRONTEND_URL:
    ALLOWED_ORIGINS.append(FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"

if not TEST_MODE and not OPENAI_API_KEY:
    logger.error("OPENAI_API_KEY environment variable is not set")
    raise ValueError("OPENAI_API_KEY environment variable is required")

if not TEST_MODE:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    logger.info("🧪 RUNNING IN TEST MODE - Using mock affirmations")
    client = None

# Request/Response Models
class AffirmationRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    feeling: str = Field(..., min_length=1, max_length=500)
    
    @field_validator('name', 'feeling')
    @classmethod
    def validate_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Field cannot be empty or whitespace only')
        return v.strip()

class AffirmationResponse(BaseModel):
    affirmation: str

class ErrorResponse(BaseModel):
    detail: str

# System prompt for safety and quality
SYSTEM_PROMPT = """You are a compassionate, supportive companion generating therapeutic affirmations.

RULES YOU MUST FOLLOW:
1. NO medical advice, diagnosis, or treatment recommendations
2. NO legal advice
3. If user expresses self-harm intent, respond with: "I hear that you're going through a difficult time. Please reach out to a mental health professional or crisis helpline. You deserve support from someone trained to help."
4. Keep responses SHORT (2-4 sentences maximum)
5. Be warm, empathetic, and personalized to the user's specific feeling
6. Focus on validation, hope, and gentle encouragement
7. Use the person's name naturally in the affirmation
8. Avoid clinical language - speak like a supportive friend

Generate a brief, heartfelt affirmation that acknowledges their feeling and offers gentle support."""

def detect_self_harm_intent(text: str) -> bool:
    """Simple keyword-based detection for self-harm expressions."""
    keywords = [
        'kill myself', 'suicide', 'end my life', 'want to die',
        'hurt myself', 'self harm', 'cutting myself', 'overdose'
    ]
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)



def generate_test_affirmation(name: str, feeling: str) -> str:
    """Generate a mock affirmation for testing without OpenAI API."""
    # Check for self-harm
    if detect_self_harm_intent(feeling):
        return (
            f"{name}, I hear that you're going through a difficult time. "
            "Please reach out to a mental health professional or crisis helpline "
            "like +27 800 567 567 (Suicide & Crisis Lifeline). You deserve support from someone "
            "trained to help. You are not alone."
        )
    
    # Different responses based on feeling keywords
    feeling_lower = feeling.lower()
    
    # ANXIOUS / STRESSED / WORRIED
    if any(word in feeling_lower for word in ['anxious', 'worried', 'nervous', 'stress']):
        affirmations = [
            f"{name}, it's completely natural to feel anxious. Your concerns are valid, "
            f"and you have the inner strength to navigate this moment. Take a deep breath—"
            f"you're more capable than you realize.",
            
            f"{name}, anxiety is your mind trying to protect you, but you're safe right now. "
            f"Ground yourself in this moment. You've overcome challenges before, and you can do it again.",
            
            f"{name}, feeling anxious shows how much you care. Channel that energy into one small, "
            f"manageable step. You don't have to have all the answers right now.",
            
            f"{name}, your anxious thoughts are just thoughts, not facts. You are stronger than your worries. "
            f"Take a moment to breathe and remind yourself: you've got this.",
            
            f"{name}, it's okay to feel uncertain. Anxiety doesn't define you or predict your future. "
            f"You have the resilience to move through this, one breath at a time."
        ]
        return random.choice(affirmations)
    
    # SAD / DOWN / DEPRESSED
    elif any(word in feeling_lower for word in ['sad', 'down', 'depressed', 'blue', 'unhappy']):
        affirmations = [
            f"{name}, I see that you're feeling down right now. These feelings are temporary, "
            f"and it's okay to not be okay sometimes. You matter, and brighter days are ahead.",
            
            f"{name}, sadness is a natural part of being human. Allow yourself to feel it without judgment. "
            f"You are worthy of compassion, especially from yourself.",
            
            f"{name}, even on your hardest days, you are enough. This feeling will pass, "
            f"and you have the strength to hold on until it does. You are not alone in this.",
            
            f"{name}, it's brave to acknowledge when you're struggling. Your feelings are valid, "
            f"and seeking support is a sign of strength, not weakness. Better days are coming.",
            
            f"{name}, sometimes we need to sit with sadness to heal. Be gentle with yourself today. "
            f"You deserve kindness and patience as you work through this moment."
        ]
        return random.choice(affirmations)
    
    # OVERWHELMED
    elif any(word in feeling_lower for word in ['overwhelm', 'too much', 'can\'t handle', 'swamped']):
        affirmations = [
            f"{name}, feeling overwhelmed shows you care deeply about what you're facing. "
            f"You don't have to do everything at once. Take it one step at a time—you've got this.",
            
            f"{name}, when everything feels like too much, focus on just one thing. "
            f"You don't have to climb the whole mountain today—just take the next step.",
            
            f"{name}, it's okay to pause and catch your breath. Being overwhelmed doesn't mean you're failing. "
            f"You're doing the best you can, and that is enough.",
            
            f"{name}, break it down into smaller pieces. You've handled difficult situations before, "
            f"and you have the capability to navigate this one too. Progress over perfection.",
            
            f"{name}, feeling overwhelmed is a sign you need to slow down, not speed up. "
            f"Give yourself permission to rest and regroup. You're stronger than you think."
        ]
        return random.choice(affirmations)
    
    # LONELY / ISOLATED
    elif any(word in feeling_lower for word in ['lonely', 'alone', 'isolated', 'disconnected']):
        affirmations = [
            f"{name}, feeling lonely is difficult, but you are worthy of connection and belonging. "
            f"Your presence matters, and there are people who care about you, even when it doesn't feel that way.",
            
            f"{name}, loneliness is a reminder of your capacity to connect deeply with others. "
            f"This feeling won't last forever, and reaching out—even in small ways—can make a difference.",
            
            f"{name}, being alone doesn't mean you're unwanted. Sometimes we need solitude to recharge. "
            f"You are valued, and connection is possible when you're ready.",
            
            f"{name}, your feelings of loneliness are valid. You deserve meaningful connections, "
            f"and they will come. In the meantime, be the friend to yourself that you need right now.",
            
            f"{name}, loneliness can feel heavy, but it's temporary. You are not invisible. "
            f"Your story matters, and there are people who will appreciate the real you."
        ]
        return random.choice(affirmations)
    
    # TIRED / EXHAUSTED
    elif any(word in feeling_lower for word in ['tired', 'exhausted', 'worn out', 'drained', 'fatigued']):
        affirmations = [
            f"{name}, it's okay to feel tired—you've been carrying a lot. "
            f"Rest is not weakness; it's necessary. Be gentle with yourself as you recharge.",
            
            f"{name}, exhaustion is your body's way of asking for care. Listen to it. "
            f"Taking time to rest is an investment in your well-being, not a luxury.",
            
            f"{name}, you've been running on empty. Give yourself permission to slow down and restore your energy. "
            f"You can't pour from an empty cup—refill yours first.",
            
            f"{name}, being tired doesn't mean you're weak. It means you've been strong for too long. "
            f"Rest, recover, and trust that you'll have the energy you need when you're ready.",
            
            f"{name}, fatigue is a signal, not a failure. Honor what your mind and body are telling you. "
            f"You deserve rest and renewal without guilt or apology."
        ]
        return random.choice(affirmations)
    
    # ANGRY / FRUSTRATED
    elif any(word in feeling_lower for word in ['angry', 'frustrated', 'mad', 'irritated', 'annoyed']):
        affirmations = [
            f"{name}, your anger is valid—it's telling you that something matters to you. "
            f"Channel that energy constructively. You have the power to address what's bothering you.",
            
            f"{name}, frustration often means you care deeply about the outcome. "
            f"Take a breath, step back if you need to, and approach this with fresh perspective.",
            
            f"{name}, it's okay to feel angry. Don't suppress it—acknowledge it, understand it, "
            f"and then decide how you want to respond. You're in control of your actions.",
            
            f"{name}, anger can be a powerful motivator for change. Use this feeling to identify "
            f"what needs to shift, then take intentional action when you're ready.",
            
            f"{name}, feeling frustrated is human. It's a sign you've been trying hard. "
            f"Give yourself credit for your effort, and remember that setbacks don't erase progress."
        ]
        return random.choice(affirmations)
    
    # HAPPY / GRATEFUL / HOPEFUL
    elif any(word in feeling_lower for word in ['happy', 'grateful', 'good', 'great', 'hopeful', 'joyful', 'excited']):
        affirmations = [
            f"{name}, it's wonderful that you're feeling {feeling}! "
            f"Take a moment to appreciate this feeling and carry this positive energy forward. "
            f"You deserve these moments of joy.",
            
            f"{name}, embrace this happiness fully! Positive moments like these are reminders "
            f"of what's possible. Let this feeling fuel your next steps forward.",
            
            f"{name}, your joy is contagious and valid. Celebrate this feeling—you've earned it. "
            f"May this positive energy continue to grow and inspire you.",
            
            f"{name}, gratitude and happiness go hand in hand. Hold onto this feeling and remember: "
            f"you have the power to create more moments like this.",
            
            f"{name}, feeling good is something to honor. Don't diminish your happiness—"
            f"you deserve to feel this way. Let it remind you of your resilience and strength."
        ]
        return random.choice(affirmations)
    
    # SCARED / AFRAID / FEARFUL
    elif any(word in feeling_lower for word in ['scared', 'afraid', 'fearful', 'terrified', 'frightened']):
        affirmations = [
            f"{name}, it's okay to feel scared. Fear is your mind protecting you. "
            f"You are braver than you think, and you can face this one moment at a time.",
            
            f"{name}, fear is natural, but it doesn't have to control you. "
            f"You've faced uncertainty before and made it through. You can do it again.",
            
            f"{name}, being afraid doesn't make you weak—it makes you human. "
            f"Courage isn't the absence of fear; it's moving forward despite it. You've got this.",
            
            f"{name}, your fear is trying to keep you safe, but you're stronger than it realizes. "
            f"Take a deep breath and remind yourself: you are capable of handling what comes.",
            
            f"{name}, fear can feel paralyzing, but you don't have to face it alone. "
            f"Reach out if you need to. Small steps forward are still steps forward."
        ]
        return random.choice(affirmations)
    
    # CONFUSED / UNCERTAIN
    elif any(word in feeling_lower for word in ['confused', 'uncertain', 'lost', 'unsure', 'stuck']):
        affirmations = [
            f"{name}, feeling confused is part of growth. You don't need all the answers right now. "
            f"Trust that clarity will come as you move forward, one step at a time.",
            
            f"{name}, uncertainty can be uncomfortable, but it also means you're open to possibilities. "
            f"Give yourself permission not to know everything yet. You're exactly where you need to be.",
            
            f"{name}, being lost doesn't mean you're doing it wrong. Sometimes we need to wander "
            f"to find our way. Trust the process—you'll find your direction.",
            
            f"{name}, confusion is often the first step toward understanding. "
            f"Be patient with yourself as things become clearer. You're figuring it out.",
            
            f"{name}, it's okay not to have it all figured out. No one does. "
            f"What matters is that you keep showing up and trying. That's enough."
        ]
        return random.choice(affirmations)
    
    # DEFAULT - For any other feeling
    else:
        affirmations = [
            f"{name}, I hear that you're feeling {feeling}. Your feelings are valid and important. "
            f"You have the strength within you to work through this moment. Take care of yourself—you're doing better than you think.",
            
            f"{name}, whatever you're experiencing right now, know that it's okay to feel this way. "
            f"Your emotions are messengers. Listen to them with compassion and move forward with courage.",
            
            f"{name}, feelings come and go like waves. This one will pass too. "
            f"In the meantime, be kind to yourself. You're navigating this the best you can.",
            
            f"{name}, thank you for being honest about how you're feeling. "
            f"That takes courage. Remember: you don't have to face this alone, and you are worthy of support.",
            
            f"{name}, your emotional experience is uniquely yours, and it matters. "
            f"Honor what you're feeling, and trust that you have the inner resources to move through it."
        ]
        return random.choice(affirmations)

@app.get("/")
async def root():
    """Health check endpoint."""
    mode = "TEST MODE" if TEST_MODE else "PRODUCTION"
    return {
        "status": "healthy",
        "service": "Mood Architect API",
        "version": "1.0.0",
        "mode": mode
    }

@app.post(
    "/api/affirmation",
    response_model=AffirmationResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid input"},
        502: {"model": ErrorResponse, "description": "OpenAI API error"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def generate_affirmation(request: AffirmationRequest):
    """
    Generate a personalized therapeutic affirmation.
    
    - **name**: User's name (1-100 characters)
    - **feeling**: How the user is feeling (1-500 characters)
    """
    
    logger.info(f"Generating affirmation for user: {request.name}")
    
    # TEST MODE - Use mock affirmations
    if TEST_MODE:
        logger.info("🧪 Using test mode - generating mock affirmation")
        time.sleep(1.5)  # Simulate API delay
        affirmation = generate_test_affirmation(request.name, request.feeling)
        return AffirmationResponse(affirmation=affirmation)
    
    # PRODUCTION MODE - Use real OpenAI API
    try:
        # Check for self-harm intent
        if detect_self_harm_intent(request.feeling):
            return AffirmationResponse(
                affirmation=(
                    f"{request.name}, I hear that you're going through a difficult time. "
                    "Please reach out to a mental health professional or crisis helpline "
                    "like 988 (Suicide & Crisis Lifeline). You deserve support from someone "
                    "trained to help. You are not alone."
                )
            )
        
        # Construct the user message
        user_message = f"Name: {request.name}\nFeeling: {request.feeling}"
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.8,
            top_p=0.9
        )
        
        affirmation = response.choices[0].message.content.strip()
        logger.info(f"Successfully generated affirmation")
        
        return AffirmationResponse(affirmation=affirmation)
        
    except Exception as e:
        logger.error(f"OpenAI API error: {str(e)}")
        
        if "rate_limit" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Our service is experiencing high demand. Please try again in a moment."
            )
        elif "api_key" in str(e).lower() or "authentication" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="Service configuration error. Please contact support."
            )
        elif "timeout" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="The request took too long. Please try again."
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="Unable to generate affirmation at this time. Please try again."
            )

@app.get("/health")
async def health_check():
    """Detailed health check for monitoring."""
    mode = "TEST" if TEST_MODE else "PRODUCTION"
    return {
        "status": "healthy",
        "openai_configured": bool(OPENAI_API_KEY) if not TEST_MODE else False,
        "service": "operational",
        "mode": mode
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)