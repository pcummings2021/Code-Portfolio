import React from "react";
import ReactDOM from "react-dom/client";  // Import createRoot from react-dom/client
import { BrowserRouter, Route, Routes } from "react-router-dom";
import About from "./Components/About/About";
import Contact from "./Components/Contact/Contact";
import Skills from "./Components/Skills/Skills";
import Resume from "./Components/Resume/Resume";
import Projects from "./Components/Projects/Projects";

const root = ReactDOM.createRoot(document.getElementById('root'));  // Initialize root

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        {/* The root path ("/") should only match when the URL is exactly "/" */}
        <Route path="/" element={<About />} index />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/skills" element={<Skills />} />
        <Route path="/resume" element={<Resume />} />
        <Route path="/projects" element={<Projects />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

