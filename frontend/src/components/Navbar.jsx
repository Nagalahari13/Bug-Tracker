import { FiLayout, FiList, FiSearch, FiPlus } from "react-icons/fi";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div className="flex justify-between items-center px-6 py-4 shadow bg-white border-b">
      <div className="flex items-center space-x-6">
        <Link to="/projects">
          <h1 className="text-2xl font-bold text-indigo-600">BugTrack</h1>
        </Link>
      </div>

      <div className="flex items-center space-x-4">
        <button className="flex items-center bg-indigo-600 text-white px-4 py-2 rounded-xl shadow">
          <FiPlus className="mr-2" /> New Bug
        </button>
      </div>
    </div>
  );
}
