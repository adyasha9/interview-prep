import Home from './components/Home/Home';
import './App.css';
import {
  BrowserRouter as Router
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
      <Home/>
      </Router>
    
    </div>
  );
}

export default App;
