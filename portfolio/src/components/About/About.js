import React, { Component } from 'react'
import './About.css'
import {Link} from 'react-router-dom';
import Resume from "../../Resume.docx"
export default class About extends Component {
      
    render() {    
       
        return (
            <div className="about">           
          <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
           <button><img src={require('../../coolicon.png').default} alt="mode" className="coolicon"/></button>

        
    <img src={require('./artemis.png').default} alt="artemis" className="artemis"/>
      
           <ul className="list">
               <li className="list-item"><Link to="/about">ABOUT</Link></li>
               <li className="list-item"><Link to="/contact">CONTACT</Link></li>
               <li className="list-item"><Link to="/work">WORK</Link></li>
               <li className="list-item"><a href={Resume}  download>RESUME</a></li>          
         </ul>
            </div>
        )
    }

}

