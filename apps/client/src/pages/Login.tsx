
import { useState } from "react";
import type { FormEvent } from "react";
import "./Login.css";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState<
    "error" | "success" | ""
  >("");

  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    // Clear previous message
    setMessage("");
    setMessageType("");

    // Frontend validation
    if (!username.trim()) {
      setMessageType("error");
      setMessage("Please enter your email or mobile number.");
      return;
    }

    if (!password) {
      setMessageType("error");
      setMessage("Please enter your password.");
      return;
    }

    try {
      setIsLoading(true);

      /*
       * Call Auth Microservice
       *
       * React/Vite
       *     |
       *     | POST /login
       *     |
       *     v
       * Auth Service :8001
       */

      const response = await fetch(
        "http://localhost:8001/login",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            username: username,
            password: password,
          }),
        }
      );

      /*
       * Read response body.
       *
       * This is required even for a 401 response,
       * because the backend sends the error message
       * in the response body.
       */

      const data = await response.json();

      console.log("Login response:", response.status, data);

      /*
       * HTTP status determines success/failure.
       *
       * 200 OK
       *     -> Login successful
       *
       * 401 Unauthorized
       *     -> Login failed
       */

      if (response.ok) {
        setMessageType("success");
        setMessage(data.message || "Login Successful");
      } else {
        setMessageType("error");
        setMessage(data.message || "Login Failed");
      }

    } catch (error) {
      /*
       * This is different from authentication failure.
       *
       * It means React could not communicate
       * with the Auth Service.
       */

      console.error("Login request failed:", error);

      setMessageType("error");
      setMessage(
        "Unable to connect to authentication server."
      );

    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-page">

      <div className="login-card">

        {/* =================================================
            Application Logo
            ================================================= */}

        <div className="logo-container">

          <div className="logo">

            <svg
              className="logo-svg"
              viewBox="0 0 64 64"
              xmlns="http://www.w3.org/2000/svg"
              aria-label="NiketAI logo"
              role="img"
            >

              <path
                d="M13 49V20
                   C13 15.5 16.5 12 21 12
                   C24.5 12 27 14 29 17
                   L42 36V20
                   C42 15.5 45.5 12 50 12
                   V49
                   C50 51 48.5 52 46.5 52
                   C43.5 52 41.5 50.5 40 48
                   L26 28V49
                   C26 51 24.5 52 22.5 52
                   C17 52 13 51 13 49Z"
                fill="white"
              />

              <path
                d="M45 12
                   C50 5 58 5 60 5
                   C60 12 56 19 48 21
                   C46 19 45 16 45 12Z"
                fill="#d9f0df"
              />

            </svg>

          </div>

          <div className="app-name">
            Niket<span>AI</span>
          </div>

        </div>


        {/* =================================================
            Heading
            ================================================= */}

        <h1>Welcome Back</h1>

        <p className="subtitle">
          Sign in to continue to your account
        </p>


        {/* =================================================
            Login Form
            ================================================= */}

        <form onSubmit={handleLogin}>

          {/* Username */}

          <div className="form-group">

            <label htmlFor="username">
              Email / Mobile Number
            </label>

            <input
              id="username"
              type="text"
              placeholder="Enter email or mobile number"
              value={username}
              disabled={isLoading}
              onChange={(event) => {
                setUsername(event.target.value);
                setMessage("");
                setMessageType("");
              }}
            />

          </div>


          {/* Password */}

          <div className="form-group">

            <label htmlFor="password">
              Password
            </label>

            <input
              id="password"
              type="password"
              placeholder="Enter your password"
              value={password}
              disabled={isLoading}
              onChange={(event) => {
                setPassword(event.target.value);
                setMessage("");
                setMessageType("");
              }}
            />

          </div>


          {/* Forgot Password */}

          <div className="forgot-password">

            <button
              type="button"
              className="forgot-button"
              disabled={isLoading}
              onClick={() => {
                setMessageType("");
                setMessage(
                  "Password recovery will be available soon."
                );
              }}
            >
              Forgot password?
            </button>

          </div>


          {/* Login Button */}

          <button
            type="submit"
            className="login-button"
            disabled={isLoading}
          >
            {isLoading ? "Logging in..." : "Login"}
          </button>


          {/* Backend Response Message */}

          {message && (
            <div
              className={`login-message ${messageType}`}
              role="alert"
            >

              <span className="message-icon">
                {messageType === "success" ? "✓" : "!"}
              </span>

              <span>
                {message}
              </span>

            </div>
          )}

        </form>


        {/* Footer */}

        <div className="login-footer">

          <span className="footer-icon">
            ◇
          </span>

          <span>
            Secure access to your account
          </span>

        </div>

      </div>

    </div>
  );
}

export default Login;