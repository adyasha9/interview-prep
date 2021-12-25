import React, { Component , useEffect , useRef } from 'react'
import {Link} from 'react-router-dom';
import './Home.css'
import Resume from "../../Resume.docx";
import Toggle from "../Toggle"
import { TimelineMax, Power1 } from "gsap/all";

export default class Home extends Component {

    constructor(props) {
        super(props);
        this.timeline = new TimelineMax({ paused: true });
        this.state = {
            flag: false,
        };
        this.darkmode = this.darkmode.bind(this);
      }
      
      darkmode() {
        console.log('you have entered into the dark mode');
        this.setState({ flag: true });
      }
      componentDidMount() {
        this.timeline
          .from(this.header, 0.5, {
            display: "none",
            autoAlpha: 0,
            delay: 0.25,
            ease: Power1.easeIn
          })
          .from(this.content, 0.4, {
            autoAlpha: 0,
            y: 25,
            ease: Power1.easeInOut
          })
    
        this.timeline.play();
      }

      changePage = (e, destination) => {
        e.preventDefault();
        this.timeline.reverse();
        const timelineDuration = this.timeline.duration() * 1000;
        setTimeout(() => {
          this.props.history.push(destination);
        }, timelineDuration);
      };
      
    render() {    
       
        return (
            <div className="container home">  
            <table ref={table => (this.header = table)}>
  <tr>
   
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td></td>

    
  </tr>
  <tr>
  <td></td>
   
  </tr>
  <tr>
  <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    
  </tr>
   <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <Toggle/>
  </tr>
  
 
</table>  
         
        
           <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
           <button onClick={this.darkmode}><img src={require('../../coolicon.png').default} alt="mode" className="coolicon" /></button>
           <div ref={div => (this.content = div)}> 
           <h1 className="h1">ADYASHA MISHRA</h1>
           <h6 style={{color: 'rgb(151, 104, 175)'}} className="h6">FULL STACK DEVELOPER</h6>
           <img src={require('./women.png').default} alt="women" className="women"/> 
          </div>
           <ul className="list">
               <li className="list-item" onClick={e => this.changePage(e, "/about")}>ABOUT</li>
               <li className="list-item"><Link to="/experience">EXPERIENCE</Link></li>
               <li className="list-item"><Link to="/contact">CONTACT</Link></li>
               <li className="list-item"><Link to="/work">WORK</Link></li>
               <li className="list-item"><a href={Resume}  download>RESUME</a></li>           
            </ul>
            </div>
        )
    }
}

