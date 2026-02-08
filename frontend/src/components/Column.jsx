import BugCard from "./BugCard";

export default function Column({ title, color, bugs }) {
  return (
    <div className="w-80">
      <div className="flex items-center space-x-2 mb-4">
        <div className={`w-3 h-3 rounded-full ${color}`}></div>
        <h3 className="font-semibold">{title}</h3>
        <span className="text-sm text-gray-500">({bugs.length})</span>
      </div>

      <div className="space-y-4">
        {bugs.map((bug) => (
          <BugCard key={bug.id} bug={bug} />
        ))}
      </div>
    </div>
  );
}
