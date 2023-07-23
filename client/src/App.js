import "./App.css";
import InputCard from "./components/InputCard/InputCard";
import InformationCard from "./components/InformationCard/InformationCard";
function App() {
  return (
    <div className="App">
      <main className="main-wrapper">
        <InputCard />
      </main>
      <aside className="aside-wrapper">
        <InformationCard />
      </aside>
    </div>
  );
}

export default App;
