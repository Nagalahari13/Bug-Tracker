import Navbar from "../components/Navbar";
import Column from "../components/Column";

export default function Board() {
  const bugs = {
    open: [
      {
        id: "BUG-001",
        title: "Login page crashes on invalid email",
        priority: "Critical",
        tags: ["auth", "crash"],
        user: "Alex Chen",
        date: "Feb 1",
      },
      {
        id: "BUG-002",
        title: "Dashboard chart not rendering on Safari",
        priority: "High",
        tags: ["ui", "safari"],
        user: "Jordan Lee",
        date: "Feb 2",
      },
    ],

    progress: [
      {
        id: "BUG-003",
        title: "File upload progress stuck at 99%",
        priority: "Medium",
        tags: ["upload", "ui"],
        user: "Alex Chen",
        date: "Jan 28",
      },
    ],

    review: [
      {
        id: "BUG-005",
        title: "Dark mode resets on refresh",
        priority: "Low",
        tags: ["ui", "preferences"],
        user: "Sarah Miller",
        date: "Jan 25",
      },
    ],
  };

  return (
    <div className="bg-gray-50 min-h-screen">
      <Navbar />

      <div className="px-10 pt-6">
        <h1 className="text-3xl font-bold mb-6">Bug Board</h1>

        <div className="flex gap-6 overflow-x-auto pb-8">
          <Column title="Open" color="bg-blue-500" bugs={bugs.open} />
          <Column title="In Progress" color="bg-yellow-500" bugs={bugs.progress} />
          <Column title="In Review" color="bg-purple-500" bugs={bugs.review} />
        </div>
      </div>
    </div>
  );
}
