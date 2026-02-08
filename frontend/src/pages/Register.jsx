import React, { useState } from "react";
import API from "../api/api";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const nav = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const registerUser = async (e) => {
    e.preventDefault();

    await API.post("/auth/register", {
      username,
      email,
      password,
    });

    nav("/login");
  };

  return (
    <div className="flex items-center justify-center min-h-screen">
      <form
        onSubmit={registerUser}
        className="p-6 shadow-xl rounded-xl w-80 bg-white space-y-4"
      >
        <h1 className="text-2xl font-bold text-center">Register</h1>

        <input
          type="text"
          placeholder="Username"
          className="border p-2 rounded w-full"
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="email"
          placeholder="Email"
          className="border p-2 rounded w-full"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="border p-2 rounded w-full"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="bg-indigo-600 text-white w-full py-2 rounded">
          Register
        </button>
      </form>
    </div>
  );
}
