import { useState } from 'react'
import './App.css'

// Update this with your deployed backend URL
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const FEELING_PRESETS = [
  'Anxious',
  'Stressed',
  'Sad',
  'Overwhelmed',
  'Lonely',
  'Tired',
  'Hopeful',
  'Grateful'
]

function App() {
  const [name, setName] = useState('')
  const [feeling, setFeeling] = useState('')
  const [customFeeling, setCustomFeeling] = useState('')
  const [affirmation, setAffirmation] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    // Clear previous results
    setAffirmation('')
    setError('')
    
    // Validate inputs
    if (!name.trim()) {
      setError('Please enter your name')
      return
    }
    
    const finalFeeling = feeling === 'custom' ? customFeeling : feeling
    if (!finalFeeling.trim()) {
      setError('Please tell us how you\'re feeling')
      return
    }
    
    setLoading(true)
    
    try {
      const response = await fetch(`${API_URL}/api/affirmation`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: name.trim(),
          feeling: finalFeeling.trim()
        })
      })
      
      if (!response.ok) {
        // Handle different error status codes
        if (response.status === 400) {
          const data = await response.json()
          throw new Error(data.detail || 'Please check your input and try again')
        } else if (response.status === 429) {
          throw new Error('Service is busy. Please wait a moment and try again')
        } else if (response.status >= 500) {
          throw new Error('Unable to connect to the service. Please try again in a moment')
        } else {
          throw new Error('Something went wrong. Please try again')
        }
      }
      
      const data = await response.json()
      setAffirmation(data.affirmation)
      
    } catch (err) {
      console.error('Error:', err)
      setError(err.message || 'Unable to generate affirmation. Please check your connection and try again')
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setAffirmation('')
    setError('')
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1 className="title">🌟 Mood Architect</h1>
          <p className="subtitle">Your personalized affirmation companion</p>
        </header>

        <div className="card">
          {!affirmation ? (
            <form onSubmit={handleSubmit} className="form">
              <div className="form-group">
                <label htmlFor="name" className="label">
                  What's your name? *
                </label>
                <input
                  type="text"
                  id="name"
                  className="input"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Enter your name"
                  maxLength={100}
                  disabled={loading}
                />
              </div>

              <div className="form-group">
                <label htmlFor="feeling" className="label">
                  How are you feeling today? *
                </label>
                <select
                  id="feeling"
                  className="select"
                  value={feeling}
                  onChange={(e) => {
                    setFeeling(e.target.value)
                    if (e.target.value !== 'custom') {
                      setCustomFeeling('')
                    }
                  }}
                  disabled={loading}
                >
                  <option value="">Select a feeling...</option>
                  {FEELING_PRESETS.map((preset) => (
                    <option key={preset} value={preset.toLowerCase()}>
                      {preset}
                    </option>
                  ))}
                  <option value="custom">Something else...</option>
                </select>
              </div>

              {feeling === 'custom' && (
                <div className="form-group">
                  <label htmlFor="customFeeling" className="label">
                    Tell us more
                  </label>
                  <textarea
                    id="customFeeling"
                    className="textarea"
                    value={customFeeling}
                    onChange={(e) => setCustomFeeling(e.target.value)}
                    placeholder="Describe how you're feeling..."
                    maxLength={500}
                    rows={4}
                    disabled={loading}
                  />
                </div>
              )}

              {error && (
                <div className="error-message">
                  ⚠️ {error}
                </div>
              )}

              <button
                type="submit"
                className={`button ${loading ? 'button-loading' : ''}`}
                disabled={loading}
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Creating your affirmation...
                  </>
                ) : (
                  '✨ Generate Affirmation'
                )}
              </button>
            </form>
          ) : (
            <div className="result">
              <div className="affirmation-box">
                <div className="affirmation-icon">💝</div>
                <p className="affirmation-text">{affirmation}</p>
              </div>
              <button onClick={handleReset} className="button button-secondary">
                Create Another
              </button>
            </div>
          )}
        </div>

        <footer className="footer">
          <p className="disclaimer">
            This tool provides supportive messages, not medical or mental health advice.
            If you're experiencing a crisis, please contact a mental health professional
            or call 988 (Suicide & Crisis Lifeline).
          </p>
        </footer>
      </div>
    </div>
  )
}

export default App
