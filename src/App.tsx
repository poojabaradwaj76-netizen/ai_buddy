import { useState, useEffect } from "react";
import { 
  BookOpen, 
  Award, 
  CheckCircle2, 
  XCircle, 
  AlertTriangle, 
  Brain, 
  Compass, 
  HelpCircle, 
  Menu, 
  X, 
  RefreshCw, 
  Play, 
  FileText, 
  Lightbulb, 
  Heart,
  ChevronRight,
  Sparkles,
  Layers,
  Activity as ActivityIcon
} from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { 
  explainTopic, 
  realLifeExample, 
  generateQuiz, 
  evaluateAnswer, 
  fullLearningSession, 
  OFFLINE_DATA,
  QuizQuestion,
  EvaluationResult,
  LearningSession
} from "./offline_data";

export default function App() {
  // Input states
  const [topic, setTopic] = useState("");
  const [activity, setActivity] = useState("Explain Topic");
  const [userAnswerText, setUserAnswerText] = useState("");
  
  // Sidebar state for mobile responsiveness
  const [sidebarOpen, setSidebarOpen] = useState(false);
  
  // UI Display states
  const [generatedTopic, setGeneratedTopic] = useState("");
  const [generatedActivity, setGeneratedActivity] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  
  // Results states
  const [explanationResult, setExplanationResult] = useState("");
  const [exampleResult, setExampleResult] = useState("");
  const [quizQuestions, setQuizQuestions] = useState<QuizQuestion[]>([]);
  const [selectedQuizAnswers, setSelectedQuizAnswers] = useState<Record<number, string>>({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  
  // Grader states
  const [graderResult, setGraderResult] = useState<EvaluationResult | null>(null);
  
  // Full session states
  const [sessionResult, setSessionResult] = useState<LearningSession | null>(null);
  const [sessionQuizAnswers, setSessionQuizAnswers] = useState<Record<number, string>>({});
  const [sessionQuizSubmitted, setSessionQuizSubmitted] = useState<Record<number, boolean>>({});

  // List of high-quality predefined study topics for recommendation
  const recommendedTopics = [
    "Binary Search",
    "Binary Tree",
    "DBMS",
    "Python",
    "Photosynthesis",
    "Machine Learning",
    "Sorting",
    "Stack",
    "Queue",
    "Operating System",
    "Computer Networks"
  ];

  // Activities descriptor mapping for Bento layout
  const activitiesList = [
    { id: "Explain Topic", label: "Explain Topic", icon: "🔍", desc: "Theoretical breakdown" },
    { id: "Real-Life Example", label: "Real-Life Example", icon: "📖", desc: "Analogies & metaphors" },
    { id: "Generate Quiz", label: "Generate Quiz", icon: "✏️", desc: "Interactive MCQs" },
    { id: "Evaluate My Answer", label: "Evaluate My Answer", icon: "📈", desc: "Smart rule-based feedback" },
    { id: "Full Learning Session", label: "Full Learning Session", icon: "🎓", desc: "All-in-one workbook" }
  ];

  // Load a quick topic helper
  const handleQuickTopic = (title: string) => {
    setTopic(title);
    handleGenerate(title, activity);
  };

  // Main generator function
  const handleGenerate = (currentTopic: string, currentActivity: string) => {
    if (!currentTopic.trim()) {
      return;
    }
    
    setIsGenerating(true);
    
    // Simulate minor lag to match Streamlit's friendly loading feedback
    setTimeout(() => {
      setGeneratedTopic(currentTopic);
      setGeneratedActivity(currentActivity);
      
      if (currentActivity === "Explain Topic") {
        setExplanationResult(explainTopic(currentTopic));
      } else if (currentActivity === "Real-Life Example") {
        setExampleResult(realLifeExample(currentTopic));
      } else if (currentActivity === "Generate Quiz") {
        setQuizQuestions(generateQuiz(currentTopic));
        setSelectedQuizAnswers({});
        setQuizSubmitted(false);
      } else if (currentActivity === "Evaluate My Answer") {
        // Evaluate user's answer
        setGraderResult(null);
      } else if (currentActivity === "Full Learning Session") {
        const ses = fullLearningSession(currentTopic);
        setSessionResult(ses);
        setSessionQuizAnswers({});
        setSessionQuizSubmitted({});
      }
      
      setIsGenerating(false);
    }, 400);
  };

  const handleEvaluateAnswer = () => {
    if (!userAnswerText.trim()) {
      alert("Please write your answer explanation first!");
      return;
    }
    const res = evaluateAnswer(generatedTopic || topic, userAnswerText);
    setGraderResult(res);
  };

  // Handle quiz radio choice
  const selectQuizOption = (qIdx: number, option: string) => {
    if (quizSubmitted) return;
    setSelectedQuizAnswers(prev => ({
      ...prev,
      [qIdx]: option
    }));
  };

  // Handle inline full session quiz selection
  const selectSessionQuizOption = (qIdx: number, option: string) => {
    setSessionQuizAnswers(prev => ({
      ...prev,
      [qIdx]: option
    }));
  };

  // Helper function to extract topic-specific stats dynamically for Bento layout
  const getTopicStats = (title: string) => {
    const lower = (title || "").toLowerCase();
    if (lower.includes("binary search")) {
      return [
        { value: "O(log n)", label: "Complexity" },
        { value: "Sorted", label: "Requirement" },
        { value: "Divide", label: "Approach" }
      ];
    } else if (lower.includes("binary tree")) {
      return [
        { value: "O(n)", label: "Complexity" },
        { value: "Pointers", label: "Structure" },
        { value: "Recursive", label: "Traversal" }
      ];
    } else if (lower.includes("dbms")) {
      return [
        { value: "O(1) Avg", label: "Index Cost" },
        { value: "ACID", label: "Compliance" },
        { value: "SQL/NoSQL", label: "Query Engine" }
      ];
    } else if (lower.includes("sorting")) {
      return [
        { value: "O(n log n)", label: "Average Time" },
        { value: "In-Place", label: "Memory" },
        { value: "Compare", label: "Mechanism" }
      ];
    } else if (lower.includes("stack") || lower.includes("queue")) {
      return [
        { value: "O(1)", label: "Access Cost" },
        { value: "LIFO/FIFO", label: "Order" },
        { value: "Array/List", label: "Backing" }
      ];
    } else if (lower.includes("photosynthesis")) {
      return [
        { value: "6 CO₂", label: "Carbon Req" },
        { value: "Light", label: "Energy Source" },
        { value: "Chloroplast", label: "Location" }
      ];
    } else if (lower.includes("machine learning")) {
      return [
        { value: "O(N * D)", label: "Complexity" },
        { value: "Dataset", label: "Requirement" },
        { value: "Statistical", label: "Approach" }
      ];
    } else if (lower.includes("python")) {
      return [
        { value: "O(1) Access", label: "Dict Search" },
        { value: "Interpreted", label: "Execution" },
        { value: "High Level", label: "Type" }
      ];
    } else if (lower.includes("operating system")) {
      return [
        { value: "Scheduler", label: "Core Module" },
        { value: "Hardware", label: "Prerequisite" },
        { value: "Kernel Space", label: "Privilege" }
      ];
    } else if (lower.includes("computer networks")) {
      return [
        { value: "7 Layers", label: "OSI Model" },
        { value: "IP Protocol", label: "Addressing" },
        { value: "Packet Sw.", label: "Mechanism" }
      ];
    } else {
      return [
        { value: "Interactive", label: "Format" },
        { value: "Structured", label: "Syllabus" },
        { value: "Offline", label: "Access" }
      ];
    }
  };

  // Helper markdown parser to create gorgeous styled React layouts
  const parseInlineFormatting = (text: string) => {
    const parts = text.split(/\*\*([^*]+)\*\*/g);
    return parts.map((part, i) => {
      if (i % 2 === 1) {
        return (
          <strong key={i} className="font-semibold text-blue-900 bg-blue-50 px-1 py-0.5 rounded">
            {part}
          </strong>
        );
      }
      // Parse inline code like `x = 5` or math latex placeholders
      if (part.includes("`") || part.includes("$")) {
        const cleanPart = part.replace(/`/g, "").replace(/\$/g, "").replace(/\\text\{([^}]+)\}/g, "$1");
        return (
          <code key={i} className="bg-slate-150 text-purple-600 px-1.5 py-0.5 rounded font-mono text-xs">
            {cleanPart}
          </code>
        );
      }
      return part;
    });
  };

  const renderMarkdown = (text: string) => {
    if (!text) return null;
    return text.split("\n").map((line, idx) => {
      const trimmedLine = line.trim();
      if (!trimmedLine) return <div key={idx} className="h-3" />;
      
      // Headers
      if (trimmedLine.startsWith("### ")) {
        return (
          <h3 key={idx} className="text-xl font-extrabold text-slate-900 mt-6 mb-3 border-b pb-1 border-slate-150 flex items-center gap-2">
            <span className="w-1.5 h-6 bg-blue-600 rounded-full"></span>
            {trimmedLine.substring(4)}
          </h3>
        );
      }
      if (trimmedLine.startsWith("#### ")) {
        return (
          <h4 key={idx} className="text-md font-bold text-slate-800 mt-4 mb-2">
            {trimmedLine.substring(5)}
          </h4>
        );
      }
      
      // Unordered Lists
      if (trimmedLine.startsWith("* ") || trimmedLine.startsWith("- ")) {
        return (
          <div key={idx} className="flex items-start gap-2.5 ml-4 my-2">
            <span className="text-blue-500 mt-1.5 text-xs font-bold">•</span>
            <span className="text-slate-600 leading-relaxed text-sm">
              {parseInlineFormatting(trimmedLine.substring(2))}
            </span>
          </div>
        );
      }

      // Ordered Lists
      if (/^\d+\.\s/.test(trimmedLine)) {
        const num = trimmedLine.match(/^(\d+)\.\s/)?.[1];
        const content = trimmedLine.replace(/^\d+\.\s/, "");
        return (
          <div key={idx} className="flex items-start gap-2.5 ml-4 my-2.5">
            <span className="font-mono text-xs text-blue-600 bg-blue-50 px-2 py-0.5 rounded-md font-bold shrink-0">
              {num}
            </span>
            <span className="text-slate-600 leading-relaxed text-sm">
              {parseInlineFormatting(content)}
            </span>
          </div>
        );
      }
      
      // Paragraph text
      return (
        <p key={idx} className="text-slate-600 leading-relaxed text-sm mb-3">
          {parseInlineFormatting(line)}
        </p>
      );
    });
  };

  // Pre-load default study guide on mount
  useEffect(() => {
    setTopic("Binary Search");
    handleGenerate("Binary Search", "Explain Topic");
  }, []);

  return (
    <div className="flex w-full min-h-screen bg-slate-50 font-sans text-slate-800 overflow-x-hidden">
      
      {/* ==========================================
          SIDEBAR (BENTO GRID DESIGN THEME)
         ========================================== */}
      {/* Mobile Backdrop */}
      <AnimatePresence>
        {sidebarOpen && (
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSidebarOpen(false)}
            className="fixed inset-0 z-50 bg-black/40 lg:hidden"
            id="mobile-backdrop"
          />
        )}
      </AnimatePresence>

      <aside className={`
        fixed inset-y-0 left-0 z-50 w-72 h-screen bg-white border-r border-slate-200 flex flex-col p-6 sticky top-0 shrink-0 transform transition-transform duration-300 ease-in-out lg:translate-x-0
        ${sidebarOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"}
      `} id="bento-sidebar">
        {/* Mobile Header for Sidebar */}
        <div className="flex items-center justify-between lg:hidden mb-4">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Navigation Menu</span>
          <button 
            onClick={() => setSidebarOpen(false)}
            className="p-1.5 hover:bg-slate-100 rounded-lg text-slate-500 border border-slate-150 bg-white"
            id="close-sidebar-btn"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="space-y-6 flex-1 overflow-y-auto pr-1">
          {/* Logo & Headline */}
          <div className="text-center pb-5 border-b border-slate-100">
            <div className="w-16 h-16 rounded-2xl bg-slate-50 border border-slate-150 flex items-center justify-center text-3xl mx-auto shadow-sm mb-3">
              🤖
            </div>
            <h2 className="font-extrabold text-slate-900 text-lg tracking-tight">AI Learning Buddy</h2>
            <p className="text-xs text-slate-500 font-medium mt-0.5">Your 24/7 Offline Tutor</p>
          </div>

          {/* About Section */}
          <div className="space-y-2.5">
            <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider">About</h3>
            <p className="text-sm text-slate-600 leading-relaxed bg-slate-50/50 border border-slate-100 p-4 rounded-2xl">
              AI Learning Buddy is your offline intelligent tutor designed to simplify complex concepts and test your knowledge through rule-based logic.
            </p>
          </div>

          {/* Features Section */}
          <div className="space-y-2.5">
            <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider">Features</h3>
            <ul className="space-y-2">
              <li className="flex items-center text-sm text-slate-600">
                <span className="w-1.5 h-1.5 bg-blue-500 rounded-full mr-2.5 shrink-0"></span>
                <span>Concept Explanations</span>
              </li>
              <li className="flex items-center text-sm text-slate-600">
                <span className="w-1.5 h-1.5 bg-purple-500 rounded-full mr-2.5 shrink-0"></span>
                <span>Real-Life Examples</span>
              </li>
              <li className="flex items-center text-sm text-slate-600">
                <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full mr-2.5 shrink-0"></span>
                <span>Interactive Quizzes</span>
              </li>
              <li className="flex items-center text-sm text-slate-600">
                <span className="w-1.5 h-1.5 bg-amber-500 rounded-full mr-2.5 shrink-0"></span>
                <span>Answer Evaluation</span>
              </li>
            </ul>
          </div>

          {/* Responsible AI Disclaimer Block */}
          <div className="p-4 bg-amber-50 border border-amber-100 rounded-2xl space-y-2 shadow-sm">
            <div className="flex items-center mb-1">
              <AlertTriangle className="w-4 h-4 text-amber-600 mr-2 shrink-0" />
              <span className="text-xs font-extrabold text-amber-800 uppercase tracking-wider">Responsible AI</span>
            </div>
            <ul className="text-[11px] text-amber-700 space-y-1.5 list-disc ml-3.5 leading-relaxed font-medium">
              <li>AI can make mistakes.</li>
              <li>Verify important information.</li>
              <li>Use AI to support learning.</li>
              <li>Don't depend on AI for exams.</li>
            </ul>
          </div>
        </div>

        {/* Footer info */}
        <div className="pt-4 border-t border-slate-100 mt-auto">
          <p className="text-xs text-slate-400 font-medium text-center italic flex items-center justify-center gap-1">
            Developed by Pooja <Heart className="w-3 h-3 text-rose-500 fill-rose-500" />
          </p>
        </div>
      </aside>

      {/* ==========================================
          MAIN CONTENT VIEWPORT
         ========================================== */}
      <main className="flex-1 flex flex-col min-h-screen p-4 md:p-8 overflow-y-auto" id="bento-main">
        
        {/* Dynamic Responsive Workspace Header */}
        <header className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8" id="main-header">
          <div className="flex items-center gap-3">
            {/* Hamburger Button for Mobile Drawer */}
            <button 
              onClick={() => setSidebarOpen(true)}
              className="p-2 hover:bg-slate-200 rounded-xl lg:hidden text-slate-600 shrink-0 border border-slate-200 bg-white shadow-sm"
              title="Open Sidebar"
              id="sidebar-toggle-main"
            >
              <Menu className="w-5 h-5" />
            </button>
            <div>
              <h1 className="text-3xl font-extrabold text-slate-900 flex items-center gap-2">
                <span className="text-2xl">🤖</span> AI Learning Buddy
              </h1>
              <p className="text-slate-500 text-sm mt-0.5">Learn anything with your personal AI tutor.</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 bg-blue-100 text-blue-700 text-xs font-extrabold rounded-full tracking-wider uppercase">OFFLINE MODE</span>
            <span className="px-3 py-1 bg-green-100 text-green-700 text-xs font-extrabold rounded-full tracking-wider uppercase flex items-center gap-1">
              <span className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse"></span>
              READY
            </span>
          </div>
        </header>

        {/* Dynamic Study Lounge Gradient Banner */}
        <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 rounded-3xl p-6 md:p-8 text-white shadow-md mb-6 relative overflow-hidden" id="study-banner">
          <div className="absolute right-0 bottom-0 top-0 w-1/3 opacity-5 flex items-center justify-center pointer-events-none">
            <Brain className="w-48 h-48 text-white" />
          </div>
          <div className="max-w-2xl relative z-10 space-y-2">
            <span className="bg-indigo-500/20 text-indigo-300 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-widest border border-indigo-500/20">
              Study Lounge
            </span>
            <h2 className="text-2xl md:text-3xl font-extrabold tracking-tight text-white leading-tight">
              Master Complex Concepts Instantly
            </h2>
            <p className="text-slate-300 text-sm md:text-base leading-relaxed">
              Enter any learning topic or choose from the expert-curated syllabus guides below. Access custom technical breakdowns, mental analogies, diagnostic check tests, and evaluations.
            </p>
          </div>
        </div>

        {/* Curated Bento Topic Picker Panel */}
        <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-200 mb-6 space-y-3.5" id="curated-panel">
          <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-blue-500" />
            Curated Study Guides:
          </h3>
          <div className="flex flex-wrap gap-2">
            {recommendedTopics.map(title => {
              const isActive = (generatedTopic.toLowerCase() === title.toLowerCase()) || (topic.toLowerCase() === title.toLowerCase() && !generatedTopic);
              return (
                <button
                  key={title}
                  onClick={() => handleQuickTopic(title)}
                  className={`
                    px-3.5 py-2 rounded-xl text-xs font-bold transition-all border
                    ${isActive 
                      ? "bg-blue-600 text-white border-blue-600 shadow-md shadow-blue-100 scale-102" 
                      : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100 hover:border-slate-300"}
                  `}
                  id={`recommend-topic-${title.replace(/\s+/g, "-")}`}
                >
                  {title}
                </button>
              );
            })}
          </div>
        </div>

        {/* Bento Grid Controls Section */}
        <div className="grid grid-cols-12 gap-6 mb-8" id="bento-controls">
          {/* Main Input and Activity Select Grid Card */}
          <div className="col-span-12 bg-white rounded-3xl p-6 shadow-sm border border-slate-200" id="controls-bento-card">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              
              {/* Input details */}
              <div className="space-y-4">
                <div className="space-y-1">
                  <label className="block text-sm font-extrabold text-slate-700">What do you want to learn today?</label>
                  <p className="text-xs text-slate-400">Type any concept or select a topic from above</p>
                </div>
                
                <div className="relative">
                  <input 
                    type="text" 
                    placeholder="Enter a topic (Example: Binary Search)" 
                    className="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:ring-2 focus:ring-blue-500 focus:outline-none transition-all placeholder:text-slate-400 text-slate-800 font-medium" 
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    id="topic-input-field"
                  />
                  {topic && (
                    <button 
                      onClick={() => setTopic("")}
                      className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1 rounded-full hover:bg-slate-200 transition-all"
                      id="clear-topic-btn"
                    >
                      <X className="w-4 h-4" />
                    </button>
                  )}
                </div>

                <button 
                  onClick={() => handleGenerate(topic, activity)}
                  disabled={!topic.trim() || isGenerating}
                  className={`w-full font-bold py-4 px-6 rounded-2xl shadow-lg transition-all flex items-center justify-center gap-2 active:scale-98
                    ${(!topic.trim() || isGenerating)
                      ? "bg-slate-200 text-slate-400 shadow-none cursor-not-allowed"
                      : "bg-purple-600 hover:bg-purple-700 text-white shadow-purple-100 hover:shadow-purple-200 hover:shadow-xl cursor-pointer"
                    }
                  `}
                  id="generate-materials-btn"
                >
                  {isGenerating ? (
                    <>
                      <RefreshCw className="w-4 h-4 animate-spin" />
                      <span>Generating Insight...</span>
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4 fill-white" />
                      <span>Generate Insight</span>
                    </>
                  )}
                </button>
              </div>

              {/* Selector Activites list */}
              <div className="space-y-3">
                <label className="block text-sm font-extrabold text-slate-700">Select Activity</label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5" id="activities-button-grid">
                  {activitiesList.map((act) => {
                    const isSelected = activity === act.id;
                    const isFullSession = act.id === "Full Learning Session";
                    return (
                      <button
                        key={act.id}
                        onClick={() => {
                          setActivity(act.id);
                          // Reactively generate the workspace if a topic is already generated
                          if (generatedTopic) {
                            handleGenerate(generatedTopic, act.id);
                          }
                        }}
                        className={`p-3 text-left rounded-2xl border transition-all flex flex-col justify-between h-18
                          ${isSelected 
                            ? "border-blue-500 bg-blue-50/70 text-blue-800 ring-2 ring-blue-500/20" 
                            : "border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50 text-slate-700"
                          }
                          ${isFullSession ? "sm:col-span-2" : "col-span-1"}
                        `}
                        id={`activity-btn-${act.id.replace(/\s+/g, "-")}`}
                      >
                        <div className="flex items-center gap-1.5">
                          <span className="text-base shrink-0">{act.icon}</span>
                          <span className="text-xs font-extrabold uppercase tracking-tight">{act.label}</span>
                        </div>
                        <p className={`text-[10px] truncate ${isSelected ? "text-blue-600 font-medium" : "text-slate-400"}`}>
                          {act.desc}
                        </p>
                      </button>
                    );
                  })}
                </div>
              </div>

            </div>

            {/* Answer Essay Entry Box - Visible only for "Evaluate My Answer" inside the Setup Controls */}
            {activity === "Evaluate My Answer" && (
              <div className="space-y-2 mt-6 pt-6 border-t border-slate-100" id="answer-essay-box">
                <label className="block text-sm font-extrabold text-slate-700 flex flex-col sm:flex-row sm:items-center justify-between gap-1">
                  <span>✍️ Enter Your Explanation or Summary of {topic || "the topic"}:</span>
                  <span className="text-xs font-normal text-slate-400">At least 1-2 paragraphs recommended</span>
                </label>
                <textarea
                  value={userAnswerText}
                  onChange={(e) => setUserAnswerText(e.target.value)}
                  placeholder={`Write your understanding here. E.g., "Binary Search works by repeatedly dividing a sorted list in half. We check the middle element..."`}
                  rows={4}
                  className="w-full p-4 border border-slate-200 bg-slate-50/50 rounded-2xl text-slate-800 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-inner placeholder:text-slate-400 leading-relaxed"
                  id="essay-input-textarea"
                />
              </div>
            )}
          </div>
        </div>

        {/* ==========================================
            OUTPUT DISPLAYS BENTO GRID STRUCTURE
           ========================================== */}
        {generatedTopic && (
          <div className="space-y-6" id="bento-outputs-container">
            
            {/* Header / Meta Info */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2 border-b border-slate-200">
              <div className="space-y-1">
                <h3 className="text-xs font-extrabold text-slate-400 uppercase tracking-widest">
                  Study Output Pane
                </h3>
                <p className="text-xl font-black text-slate-900 tracking-tight">
                  Tutor Material for <span className="text-blue-600 font-extrabold">{generatedTopic}</span>
                </p>
              </div>
              
              <span className="text-xs text-slate-500 flex items-center gap-1.5 bg-white border border-slate-200 px-3 py-1.5 rounded-xl shadow-sm self-start">
                <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse shrink-0"></span>
                <span>Active Concept Sandbox</span>
              </span>
            </div>

            {isGenerating ? (
              <div className="bg-white rounded-3xl p-16 border border-slate-200 text-center space-y-4 shadow-sm" id="loading-fallback">
                <RefreshCw className="w-10 h-10 text-blue-500 animate-spin mx-auto" />
                <p className="text-sm text-slate-600 font-bold">Assembling premium templates offline...</p>
              </div>
            ) : (
              <div className="grid grid-cols-12 gap-6" id="output-bento-grid">
                
                {/* 1. Main Output Display Box (Span 8) */}
                <div className="col-span-12 lg:col-span-8 bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-200 flex flex-col" id="main-output-pane">
                  
                  {/* Dynamic Output Header */}
                  <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-100">
                    <h2 className="text-lg font-extrabold text-slate-900 flex items-center gap-2">
                      <span className="text-blue-600">
                        {generatedActivity === "Explain Topic" && <BookOpen className="w-5 h-5" />}
                        {generatedActivity === "Real-Life Example" && <Lightbulb className="w-5 h-5" />}
                        {generatedActivity === "Generate Quiz" && <FileText className="w-5 h-5" />}
                        {generatedActivity === "Evaluate My Answer" && <Award className="w-5 h-5" />}
                        {generatedActivity === "Full Learning Session" && <Layers className="w-5 h-5" />}
                      </span>
                      <span>{generatedActivity} Result</span>
                    </h2>
                    <span className="text-[10px] font-extrabold text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full uppercase tracking-wider">
                      TOPIC: {generatedTopic.toUpperCase()}
                    </span>
                  </div>

                  {/* Dynamic Content Views */}
                  <div className="flex-1 space-y-4" id="view-content-wrapper">
                    
                    {/* Activity 1: Explain Topic */}
                    {generatedActivity === "Explain Topic" && explanationResult && (
                      <motion.div 
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="space-y-4"
                        id="explain-topic-view"
                      >
                        <div className="prose max-w-none text-slate-700 leading-relaxed">
                          {renderMarkdown(explanationResult)}
                        </div>
                      </motion.div>
                    )}

                    {/* Activity 2: Real Life Example */}
                    {generatedActivity === "Real-Life Example" && exampleResult && (
                      <motion.div 
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="space-y-4"
                        id="real-life-view"
                      >
                        <div className="prose max-w-none text-slate-700 leading-relaxed">
                          {renderMarkdown(exampleResult)}
                        </div>
                      </motion.div>
                    )}

                    {/* Activity 3: Generate Quiz */}
                    {generatedActivity === "Generate Quiz" && quizQuestions.length > 0 && (
                      <motion.div 
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="space-y-6"
                        id="generate-quiz-view"
                      >
                        <div className="p-4 bg-slate-50 border border-slate-100 rounded-2xl text-xs space-y-1">
                          <h4 className="font-bold text-slate-800 flex items-center gap-1">
                            <span>✏️</span> Multiple-Choice Challenge
                          </h4>
                          <p className="text-slate-500">Choose the correct answer for all 5 questions below and check your score results.</p>
                        </div>

                        <div className="space-y-5">
                          {quizQuestions.map((q, qIdx) => (
                            <div key={qIdx} className="border border-slate-150 rounded-2xl p-5 bg-white shadow-sm space-y-3.5" id={`quiz-question-card-${qIdx}`}>
                              <h5 className="font-extrabold text-slate-800 text-sm flex items-start gap-2">
                                <span className="bg-blue-100 text-blue-800 text-[10px] px-2 py-0.5 rounded font-mono font-black shrink-0">
                                  Q{qIdx + 1}
                                </span>
                                <span className="leading-snug">{q.question}</span>
                              </h5>

                              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-1" id={`quiz-options-${qIdx}`}>
                                {Object.entries(q.options).map(([letter, text]) => {
                                  const isSelected = selectedQuizAnswers[qIdx] === letter;
                                  const isCorrectOpt = q.correct_answer === letter;
                                  
                                  let optionStyle = "border-slate-200 bg-white hover:bg-slate-50 text-slate-700";
                                  if (isSelected) {
                                    optionStyle = "border-blue-500 bg-blue-50/75 ring-2 ring-blue-500/20 text-blue-900 font-semibold";
                                  }
                                  
                                  if (quizSubmitted) {
                                    if (isCorrectOpt) {
                                      optionStyle = "border-emerald-500 bg-emerald-50 text-emerald-900 font-extrabold ring-2 ring-emerald-500/20";
                                    } else if (isSelected && !isCorrectOpt) {
                                      optionStyle = "border-rose-500 bg-rose-50 text-rose-900 font-semibold ring-2 ring-rose-500/20";
                                    } else {
                                      optionStyle = "border-slate-200 opacity-60 text-slate-500 bg-white";
                                    }
                                  }

                                  return (
                                    <button
                                      key={letter}
                                      disabled={quizSubmitted}
                                      onClick={() => selectQuizOption(qIdx, letter)}
                                      className={`
                                        text-left p-3.5 rounded-xl border text-xs transition-all flex items-start gap-2.5
                                        ${optionStyle}
                                        ${quizSubmitted ? "cursor-default" : "cursor-pointer active:scale-[0.98]"}
                                      `}
                                      id={`q-${qIdx}-opt-${letter}`}
                                    >
                                      <span className={`
                                        w-5 h-5 rounded-md flex items-center justify-center font-mono text-xs font-bold border shrink-0
                                        ${isSelected ? "bg-blue-600 text-white border-blue-600" : "bg-slate-50 text-slate-500 border-slate-300"}
                                        ${quizSubmitted && isCorrectOpt ? "bg-emerald-600 text-white border-emerald-600" : ""}
                                        ${quizSubmitted && isSelected && !isCorrectOpt ? "bg-rose-600 text-white border-rose-600" : ""}
                                      `}>
                                        {letter}
                                      </span>
                                      <span className="leading-snug">{text}</span>
                                    </button>
                                  );
                                })}
                              </div>

                              {/* Question Feedback Reasoning info */}
                              {quizSubmitted && (
                                <div className={`
                                  p-4 rounded-xl text-xs flex gap-2.5 border transition-all duration-300
                                  ${selectedQuizAnswers[qIdx] === q.correct_answer 
                                    ? "bg-emerald-50/50 border-emerald-150 text-emerald-800" 
                                    : "bg-rose-50/50 border-rose-150 text-rose-800"}
                                `} id={`quiz-feedback-${qIdx}`}>
                                  {selectedQuizAnswers[qIdx] === q.correct_answer ? (
                                    <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" />
                                  ) : (
                                    <XCircle className="w-5 h-5 text-rose-600 shrink-0 mt-0.5" />
                                  )}
                                  <div className="space-y-1">
                                    <p className="font-extrabold text-[13px]">
                                      {selectedQuizAnswers[qIdx] === q.correct_answer ? "Correct Response" : "Incorrect Response"}
                                    </p>
                                    <p className="leading-relaxed text-slate-600">{q.explanation}</p>
                                  </div>
                                </div>
                              )}
                            </div>
                          ))}
                        </div>

                        {/* Submit Actions */}
                        {!quizSubmitted ? (
                          <div className="flex justify-center pt-4" id="quiz-submit-action">
                            <button
                              onClick={() => {
                                if (Object.keys(selectedQuizAnswers).length < 5) {
                                  alert("Please select an answer choice for all 5 questions first!");
                                  return;
                                }
                                setQuizSubmitted(true);
                              }}
                              className="bg-purple-600 hover:bg-purple-700 active:scale-95 text-white font-extrabold px-8 py-4 rounded-2xl shadow-lg shadow-purple-100 transition-all text-sm cursor-pointer"
                              id="quiz-submit-btn"
                            >
                              Submit Quiz Responses
                            </button>
                          </div>
                        ) : (
                          <div className="bg-slate-50 rounded-2xl border border-slate-200 p-6 md:p-8 text-center space-y-4 shadow-inner" id="quiz-results-pane">
                            <h4 className="text-base font-extrabold text-slate-800 uppercase tracking-wider">Your Self-Evaluation Tally</h4>
                            
                            {/* Score computation */}
                            {(() => {
                              let correctCount = 0;
                              quizQuestions.forEach((q, idx) => {
                                if (selectedQuizAnswers[idx] === q.correct_answer) {
                                  correctCount++;
                                }
                              });
                              const pct = (correctCount / 5) * 100;
                              
                              return (
                                <div className="max-w-md mx-auto space-y-4">
                                  <div className="text-5xl font-black text-blue-600 tracking-tight">
                                    {correctCount} <span className="text-2xl text-slate-400 font-medium">/ 5</span>
                                    <span className="text-lg text-slate-500 font-bold ml-2">({pct}%)</span>
                                  </div>
                                  
                                  <div className="w-full bg-slate-200 h-3 rounded-full overflow-hidden shadow-inner">
                                    <div 
                                      className="h-full bg-gradient-to-r from-blue-500 to-indigo-600 transition-all duration-700 rounded-full"
                                      style={{ width: `${pct}%` }}
                                    />
                                  </div>

                                  <p className="text-sm text-slate-600 font-bold px-4 leading-relaxed">
                                    {correctCount === 5 && "🏆 Stellar work! Perfect Score. You fully understand this topic!"}
                                    {correctCount >= 3 && correctCount < 5 && "👍 Well done! You have a solid grasp. Review explanations to aim for 5/5!"}
                                    {correctCount < 3 && "💪 Good try! Learning is iterative. Go back to the theoretical breakdowns and try again."}
                                  </p>

                                  <button
                                    onClick={() => {
                                      setSelectedQuizAnswers({});
                                      setQuizSubmitted(false);
                                    }}
                                    className="text-xs font-bold text-blue-600 bg-blue-50 hover:bg-blue-100 border border-blue-200 px-5 py-2.5 rounded-xl cursor-pointer shadow-sm transition-all mt-2"
                                    id="retake-quiz-btn"
                                  >
                                    Retake the Quiz
                                  </button>
                                </div>
                              );
                            })()}
                          </div>
                        )}
                      </motion.div>
                    )}

                    {/* Activity 4: Evaluate My Answer */}
                    {generatedActivity === "Evaluate My Answer" && (
                      <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="space-y-6"
                        id="evaluate-essay-view"
                      >
                        <div className="bg-slate-50 border border-slate-200 rounded-2xl p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                          <div>
                            <h4 className="font-bold text-slate-800 text-sm">Concept Reviewer</h4>
                            <p className="text-xs text-slate-500">Compare your written understanding against the rule-based grader.</p>
                          </div>
                          <button
                            onClick={handleEvaluateAnswer}
                            className="bg-purple-600 hover:bg-purple-700 text-white font-extrabold px-5 py-3 rounded-xl shadow-md text-xs cursor-pointer active:scale-95 transition-all self-start sm:self-center"
                            id="run-essay-evaluator-btn"
                          >
                            Evaluate Explanation
                          </button>
                        </div>

                        {!graderResult && !userAnswerText.trim() && (
                          <div className="text-center p-8 border border-dashed border-slate-200 rounded-2xl" id="empty-essay-prompt">
                            <span className="text-3xl block mb-2">✍️</span>
                            <p className="text-slate-500 text-sm font-medium">Please enter your understanding in the text block inside the Setup card above to activate this evaluation tool.</p>
                          </div>
                        )}

                        {graderResult && (
                          <div className="grid grid-cols-1 md:grid-cols-3 gap-6" id="grader-results-grid">
                            
                            {/* Radial Progress / Score Ring */}
                            <div className="bg-white rounded-2xl border border-slate-200 p-6 text-center flex flex-col justify-center items-center space-y-4 shadow-sm" id="grader-score-ring">
                              <h5 className="font-bold text-slate-400 text-xs uppercase tracking-wider">Evaluation Score</h5>
                              
                              <div className="relative w-32 h-32 flex items-center justify-center">
                                {/* SVG Circle Progress Ring */}
                                <svg className="w-full h-full transform -rotate-90">
                                  <circle 
                                    cx="64" cy="64" r="52" 
                                    stroke="#f1f5f9" strokeWidth="10" 
                                    fill="transparent" 
                                  />
                                  <circle 
                                    cx="64" cy="64" r="52" 
                                    stroke={graderResult.score >= 80 ? "#10b981" : graderResult.score >= 60 ? "#3b82f6" : "#f59e0b"} 
                                    strokeWidth="10" 
                                    fill="transparent" 
                                    strokeDasharray={2 * Math.PI * 52}
                                    strokeDashoffset={2 * Math.PI * 52 * (1 - graderResult.score / 100)}
                                    strokeLinecap="round"
                                    className="transition-all duration-1000 ease-out"
                                  />
                                </svg>
                                <div className="absolute text-3xl font-black text-slate-800 tracking-tight">
                                  {graderResult.score}
                                  <span className="text-[10px] text-slate-400 block font-bold uppercase tracking-wider">pts</span>
                                </div>
                              </div>

                              <p className="font-black text-sm text-slate-800 leading-snug">
                                {graderResult.score >= 80 ? "🌟 Excellent understanding!" : graderResult.score >= 60 ? "⚡ Good conceptual grasp!" : "📝 Keep studying!"}
                              </p>
                            </div>

                            {/* Feedbacks / Mistakes analysis */}
                            <div className="md:col-span-2 space-y-4" id="grader-feedbacks-col">
                              <div className="bg-blue-50/50 border border-blue-200 p-5 rounded-2xl space-y-1">
                                <h5 className="font-extrabold text-blue-900 text-xs uppercase tracking-wider flex items-center gap-1.5">
                                  <span className="text-base">💡</span>
                                  Primary Assessment Feedback
                                </h5>
                                <p className="text-sm text-blue-950 leading-relaxed font-semibold">
                                  {graderResult.feedback}
                                </p>
                              </div>

                              <div className="bg-rose-50/50 border border-rose-200 p-5 rounded-2xl space-y-1">
                                <h5 className="font-extrabold text-rose-900 text-xs uppercase tracking-wider flex items-center gap-1.5">
                                  <span className="text-base">🚨</span>
                                  Missed Parameters / Mistakes Detected
                                </h5>
                                <p className="text-sm text-rose-950 leading-relaxed font-semibold">
                                  {graderResult.mistakes}
                                </p>
                              </div>
                            </div>

                            {/* Actionable Suggestions */}
                            <div className="md:col-span-3 bg-slate-50 rounded-2xl border border-slate-200 p-5 space-y-4 shadow-inner" id="grader-suggestions-box">
                              <h5 className="font-extrabold text-slate-800 text-xs uppercase tracking-widest border-b pb-2 border-slate-200 flex items-center gap-2">
                                <span className="p-1 bg-purple-100 text-purple-700 rounded-lg">⚙️</span>
                                Actionable Suggestions to Improve Your Score:
                              </h5>

                              <div className="space-y-3">
                                {graderResult.suggestions.map((sug, idx) => (
                                  <div key={idx} className="flex items-start gap-2.5">
                                    <span className="bg-white border border-slate-200 text-slate-700 font-mono text-[10px] w-5 h-5 rounded flex items-center justify-center shrink-0 mt-0.5 font-bold shadow-sm">
                                      {idx + 1}
                                    </span>
                                    <p className="text-xs text-slate-600 leading-relaxed font-medium">
                                      {sug}
                                    </p>
                                  </div>
                                ))}
                              </div>

                              <div className="bg-white border border-slate-200 p-4 rounded-xl text-xs italic text-slate-600 flex items-center gap-2 shadow-sm font-medium">
                                <span className="text-lg shrink-0">💬</span>
                                <span>"{graderResult.encouragement}"</span>
                              </div>
                            </div>

                          </div>
                        )}
                      </motion.div>
                    )}

                    {/* Activity 5: Full Learning Session */}
                    {generatedActivity === "Full Learning Session" && sessionResult && (
                      <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="space-y-8"
                        id="masterclass-full-view"
                      >
                        {/* Syllabus intro info */}
                        <div className="bg-slate-50 border border-slate-200 rounded-2xl p-5 space-y-2.5 shadow-inner">
                          <div className="flex items-center gap-2.5">
                            <span className="text-3xl">🎓</span>
                            <div>
                              <h4 className="text-sm font-extrabold text-slate-800 uppercase tracking-wider">Complete Masterclass Syllabus</h4>
                              <p className="text-xs text-slate-500">Structured interactive notebook for deep integration</p>
                            </div>
                          </div>
                          <p className="text-xs text-slate-600 leading-relaxed font-medium">
                            Follow this complete workbook. We have assembled the syllabus, analogies, quick diagnostic inline questions, summaries, and customized study checkpoints below.
                          </p>
                        </div>

                        {/* Step 1: Detailed Explanation */}
                        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4" id="masterclass-step-1">
                          <div className="flex items-center justify-between pb-3 border-b border-slate-100">
                            <h5 className="font-extrabold text-slate-800 text-sm uppercase tracking-wider flex items-center gap-2">
                              <span className="bg-blue-600 text-white text-[9px] font-black font-mono px-2 py-0.5 rounded">STEP 1</span>
                              Theoretical Breakdown
                            </h5>
                            <span className="text-xs font-bold text-blue-600">Active Learning</span>
                          </div>
                          <div className="prose max-w-none text-slate-700 leading-relaxed">
                            {renderMarkdown(sessionResult.explanation)}
                          </div>
                        </div>

                        {/* Step 2: Real-Life Analogy */}
                        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4" id="masterclass-step-2">
                          <div className="flex items-center justify-between pb-3 border-b border-slate-100">
                            <h5 className="font-extrabold text-slate-800 text-sm uppercase tracking-wider flex items-center gap-2">
                              <span className="bg-emerald-600 text-white text-[9px] font-black font-mono px-2 py-0.5 rounded">STEP 2</span>
                              Mental Model Metaphor
                            </h5>
                            <span className="text-xs font-bold text-emerald-600">Intuitive Analogy</span>
                          </div>
                          <div className="prose max-w-none text-slate-700 leading-relaxed">
                            {renderMarkdown(sessionResult.real_life_example)}
                          </div>
                        </div>

                        {/* Step 3: Inline Quizzes */}
                        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4" id="masterclass-step-3">
                          <div className="pb-3 border-b border-slate-100">
                            <h5 className="font-extrabold text-slate-800 text-sm uppercase tracking-wider flex items-center gap-2">
                              <span className="bg-purple-600 text-white text-[9px] font-black font-mono px-2 py-0.5 rounded">STEP 3</span>
                              Diagnostic Checkpoint
                            </h5>
                            <p className="text-xs text-slate-400 mt-1">Check individual aspects to reinforce active retention of concepts</p>
                          </div>

                          <div className="space-y-4 pt-2">
                            {sessionResult.quiz.map((q, qIdx) => (
                              <div key={qIdx} className="border border-slate-150 rounded-2xl p-4 bg-slate-50/50 space-y-3.5" id={`session-q-card-${qIdx}`}>
                                <p className="font-extrabold text-slate-800 text-xs flex items-center gap-2">
                                  <span className="bg-slate-200 text-slate-700 px-2 py-0.5 rounded font-mono text-[9px] font-black">
                                    Q{qIdx + 1}
                                  </span>
                                  <span>{q.question}</span>
                                </p>

                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2" id={`session-q-options-${qIdx}`}>
                                  {Object.entries(q.options).map(([letter, text]) => {
                                    const isSelected = sessionQuizAnswers[qIdx] === letter;
                                    const isSubmitted = sessionQuizSubmitted[qIdx];
                                    const isCorrect = q.correct_answer === letter;

                                    let optClass = "border-slate-200 bg-white hover:bg-slate-50 text-slate-700";
                                    if (isSelected) optClass = "border-blue-500 bg-blue-50/75 ring-2 ring-blue-500/20 font-semibold";
                                    if (isSubmitted) {
                                      if (isCorrect) optClass = "border-emerald-500 bg-emerald-50 text-emerald-900 font-extrabold ring-2 ring-emerald-500/10";
                                      else if (isSelected) optClass = "border-rose-500 bg-rose-50 text-rose-900 ring-2 ring-rose-500/10";
                                      else optClass = "opacity-50 border-slate-200 bg-white";
                                    }

                                    return (
                                      <button
                                        key={letter}
                                        disabled={isSubmitted}
                                        onClick={() => selectSessionQuizOption(qIdx, letter)}
                                        className={`text-left p-3 rounded-xl border text-[11px] transition-all flex items-start gap-2 ${optClass} ${isSubmitted ? "cursor-default" : "cursor-pointer"}`}
                                        id={`session-q-${qIdx}-opt-${letter}`}
                                      >
                                        <span className="font-mono font-bold text-slate-400">{letter})</span>
                                        <span className="leading-snug">{text}</span>
                                      </button>
                                    );
                                  })}
                                </div>

                                {!sessionQuizSubmitted[qIdx] ? (
                                  <button
                                    onClick={() => {
                                      if (!sessionQuizAnswers[qIdx]) {
                                        alert("Please select an answer choice for this question!");
                                        return;
                                      }
                                      setSessionQuizSubmitted(prev => ({ ...prev, [qIdx]: true }));
                                    }}
                                    className="text-[10px] font-bold text-blue-600 hover:text-blue-800 flex items-center gap-1 mt-1 cursor-pointer hover:underline"
                                    id={`session-submit-q-btn-${qIdx}`}
                                  >
                                    Submit Question Response <ChevronRight className="w-3 h-3" />
                                  </button>
                                ) : (
                                  <div className="bg-white border border-slate-150 rounded-xl p-3 text-[11px] text-slate-600 mt-2 space-y-1 shadow-sm transition-all duration-300" id={`session-q-feedback-${qIdx}`}>
                                    <p className="font-extrabold flex items-center gap-1 text-[12px]">
                                      {sessionQuizAnswers[qIdx] === q.correct_answer ? (
                                        <span className="text-emerald-600 flex items-center gap-1">
                                          <CheckCircle2 className="w-3.5 h-3.5 shrink-0" /> Correct Choice
                                        </span>
                                      ) : (
                                        <span className="text-rose-600 flex items-center gap-1">
                                          <XCircle className="w-3.5 h-3.5 shrink-0" /> Incorrect Choice (Correct is {q.correct_answer})
                                        </span>
                                      )}
                                    </p>
                                    <p className="leading-relaxed text-slate-500">{q.explanation}</p>
                                  </div>
                                )}
                              </div>
                            ))}
                          </div>
                        </div>

                        {/* Step 4: Study guide summary & quote */}
                        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4" id="masterclass-step-4">
                          <div className="flex items-center justify-between pb-3 border-b border-slate-100">
                            <h5 className="font-extrabold text-slate-800 text-sm uppercase tracking-wider flex items-center gap-2">
                              <span className="bg-pink-600 text-white text-[9px] font-black font-mono px-2 py-0.5 rounded">STEP 4</span>
                              Review & Takeaway
                            </h5>
                            <span className="text-xs font-bold text-pink-600">Review Complete</span>
                          </div>
                          <div className="prose max-w-none text-slate-700 leading-relaxed">
                            {renderMarkdown(sessionResult.summary)}
                          </div>

                          <div className="bg-purple-50 border border-purple-150 p-5 rounded-2xl text-xs italic text-purple-900 leading-relaxed shadow-sm font-medium">
                            {sessionResult.motivational_message}
                          </div>
                        </div>

                      </motion.div>
                    )}

                  </div>

                </div>

                {/* 2. Side-Panel (Span 4) containing Bento Stats and Quick Grader */}
                <div className="col-span-12 lg:col-span-4 flex flex-col gap-6" id="side-output-pane">
                  
                  {/* Bento Stat Card: Topic Insights */}
                  <div className="bg-white border border-slate-200 p-6 rounded-3xl shadow-sm flex flex-col" id="bento-stat-insights-card">
                    <h4 className="text-xs font-black text-slate-400 uppercase tracking-widest mb-4 flex items-center gap-1.5">
                      <ActivityIcon className="w-3.5 h-3.5 text-blue-500" />
                      Topic Insights
                    </h4>
                    <div className="grid grid-cols-3 gap-2">
                      {getTopicStats(generatedTopic || topic).map((stat, sIdx) => (
                        <div key={sIdx} className="bg-slate-50 border border-slate-100 p-3 rounded-xl text-center shadow-sm flex flex-col justify-center min-h-[75px]" id={`stat-col-${sIdx}`}>
                          <p className="text-sm font-black text-blue-600 leading-tight truncate" title={stat.value}>{stat.value}</p>
                          <p className="text-[9px] text-slate-400 font-extrabold uppercase tracking-tight mt-1 leading-none">{stat.label}</p>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Quick Grader Checkpoint Panel (Contrast Dark Panel) */}
                  <div className="bg-slate-900 text-white rounded-3xl p-6 shadow-xl flex flex-col space-y-4" id="bento-dark-quickgrader">
                    <div className="space-y-1">
                      <h3 className="text-white font-black text-base tracking-tight flex items-center gap-2">
                        <span>🧠</span>
                        Quick Recall Check
                      </h3>
                      <p className="text-slate-400 text-xs">Self-explain to lock in retention</p>
                    </div>

                    <div className="space-y-4">
                      <div className="p-3.5 bg-slate-800/80 rounded-2xl border border-slate-800 text-xs text-slate-300 leading-relaxed italic">
                        "Explain how <strong>{generatedTopic || topic || "this concept"}</strong> works in your own words..."
                      </div>
                      
                      <textarea 
                        value={userAnswerText}
                        onChange={(e) => setUserAnswerText(e.target.value)}
                        placeholder="Type your summary explanation here to activate smart evaluations..." 
                        className="w-full h-32 bg-slate-800 border-none rounded-2xl p-3.5 text-xs text-slate-200 placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none font-medium leading-relaxed"
                        id="dark-evaluator-textarea"
                      />
                      
                      <button 
                        onClick={() => {
                          setActivity("Evaluate My Answer");
                          setGeneratedActivity("Evaluate My Answer");
                          handleEvaluateAnswer();
                        }}
                        className="w-full py-3.5 bg-purple-600 hover:bg-purple-700 text-white font-extrabold rounded-2xl text-xs border border-purple-500 shadow-lg shadow-purple-900/40 transition-all active:scale-[0.98] cursor-pointer text-center"
                        id="dark-evaluate-trigger-btn"
                      >
                        Activate Evaluation
                      </button>
                    </div>
                  </div>

                </div>

              </div>
            )}

          </div>
        )}

      </main>
    </div>
  );
}
