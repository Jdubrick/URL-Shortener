import "./App.css";
import InputCard from "./components/InputCard/InputCard";
import InformationCard from "./components/InformationCard/InformationCard";
import Header from "./components/Header/Header";
import { useState } from "react";
function App() {
  const [generatedShortUrl, setGeneratedShortUrl] = useState("");
  return (
    <div className="App">
      <Header />
      <div className="content">
        <InputCard setGeneratedShortUrl={setGeneratedShortUrl} />
        <InformationCard generatedShortUrl={generatedShortUrl} />
      </div>
    </div>
  );
}

export default App;
