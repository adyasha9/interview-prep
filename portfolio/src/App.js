import Home from './components/Home/Home';
import About from './components/About/About';
import Contact from './components/Contact/Contact';
import Work from './components/Work/Work';
import Experience from './components/Experience/Experience';
// import NotFound from './components/NotFound/NotFound';
import { Route} from "react-router";
import './App.css';
import {
  BrowserRouter as Router
} from "react-router-dom";

function App() {
  return (
    <div className="App">
    <Router>
    <Route exact path="/" component={Home} />
    <Route path="/about" component={About} />
    <Route path="/work" component={Work} />
    <Route path="/contact" component={Contact} />
    <Route path="/experience" component={Experience} />
    {/* <Route component={NotFound} />  */}
</Router>
    </div>
  );
}

export default App;
