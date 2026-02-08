import { useEffect, useState } from "react";
import API from "../api/api";
import Navbar from "../components/Navbar";
import { Link } from "react-router-dom";

export default function Projects() {
  const [projects, setProjects] = useState([]);

  const loadProjects = async () => {
    const res = await API.get("/projects");
    setProjects(res.data);
  };

  useEffect(() => {
    loadProjects();
  }, []);

  return (
    <>
      <Navbar />
      <div className="p-10">
        <h1 className="text-3xl font-bold mb-6">Projects</h1>

        <div className="grid grid-cols-3 gap-6">
          {projects.map((p) => (
            <Link
              to="/board"
              key={p.id}
              className="bg-white p-4 rounded-xl shadow border"
            >
              <h2 className="font-semibold text-xl">{p.name}</h2>
              <p className="text-gray-600 mt-2">{p.description}</p>
            </Link>
          ))}
        </div>
      </div>
    </>
  );
}
