import React, { useState } from "react";
import API from "../api/api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const nav = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const loginUser = async (e) => {
    e.preventDefault();

    const form = new URLSearchParams();
    form.append("username", email);
    form.append("password", password);

    const res = await API.post("/auth/login", form);

    if (res.data.access_token) {
      localStorage.setItem("token", res.data.access_token);
      nav("/projects");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen">
      <form
        onSubmit={loginUser}
        className="p-6 shadow-xl rounded-xl w-80 bg-white space-y-4"
      >
        <h1 className="text-2xl font-bold text-center">Login</h1>

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
          Login
        </button>
      </form>
    </div>
  );
}
