import React, { useState } from "react";
import "./Register.css";
import user_icon from "../assets/person.png";
import email_icon from "../assets/email.png";
import password_icon from "../assets/password.png";
import close_icon from "../assets/close.png";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [loading, setLoading] = useState(false);

  const gohome = () => {
    window.location.href = window.location.origin;
  };

  const register = async (e) => {
    e.preventDefault();

    if (!userName || !password || !email) {
      alert("⚠️ Please fill all required fields");
      return;
    }

    setLoading(true);

    let register_url = window.location.origin + "/djangoapp/register";

    try {
      const res = await fetch(register_url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userName,
          password,
          firstName,
          lastName,
          email,
        }),
      });

      const json = await res.json();

      if (json.status) {
        sessionStorage.setItem("username", json.userName);
        alert("🚀 Registration Successful!");
        window.location.href = window.location.origin;
      } else if (json.error === "Already Registered") {
        alert("❌ User already exists");
      } else {
        alert("⚠️ Something went wrong");
      }
    } catch (err) {
      alert("🔥 Server error");
    }

    setLoading(false);
  };

  return (
    <div className="register_bg">
      <div className="register_container glass">
        <div className="header">
          <h2 className="title">✨ Create Account</h2>
          <img src={close_icon} className="close_btn" onClick={gohome} alt="X" />
        </div>

        <form onSubmit={register}>
          <div className="inputs">

            <div className="input_group">
              <img src={user_icon} alt="" />
              <input placeholder="Username" onChange={(e) => setUserName(e.target.value)} />
            </div>

            <div className="input_group">
              <img src={user_icon} alt="" />
              <input placeholder="First Name" onChange={(e) => setFirstName(e.target.value)} />
            </div>

            <div className="input_group">
              <img src={user_icon} alt="" />
              <input placeholder="Last Name" onChange={(e) => setLastName(e.target.value)} />
            </div>

            <div className="input_group">
              <img src={email_icon} alt="" />
              <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            </div>

            <div className="input_group">
              <img src={password_icon} alt="" />
              <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            </div>

          </div>

          <button className="submit_btn" disabled={loading}>
            {loading ? "⏳ Registering..." : "🚀 Register"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;