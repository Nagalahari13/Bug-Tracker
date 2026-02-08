import { FiUser, FiCalendar } from "react-icons/fi";
import classNames from "classnames";

export default function BugCard({ bug }) {
  const priorityColors = {
    Critical: "bg-red-100 text-red-600",
    High: "bg-orange-100 text-orange-600",
    Medium: "bg-yellow-100 text-yellow-600",
    Low: "bg-green-100 text-green-600",
  };

  return (
    <div className="bg-white p-4 rounded-xl shadow border">
      <p className="text-xs text-gray-500">{bug.id}</p>

      <h2 className="font-semibold text-gray-800 mt-1">{bug.title}</h2>

      <span
        className={classNames(
          "text-xs px-2 py-1 rounded-lg mt-2 inline-block",
          priorityColors[bug.priority]
        )}
      >
        {bug.priority}
      </span>

      <div className="flex text-sm justify-between text-gray-500 mt-3">
        <div className="flex items-center gap-1">
          <FiUser />
          <span>{bug.user}</span>
        </div>

        <div className="flex items-center gap-1">
          <FiCalendar />
          <span>{bug.date}</span>
        </div>
      </div>
    </div>
  );
}
