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
    <div className="row">
    <p>Hey, I am a full-stack developer completing my BE at <span className="fas fa-graduation-cap"></span> SIES Graduate School Of Technology ,looking forward to getting industry exposure who loves building web applications. I have industry experience building websites and web applications. I specialize in JavaScript and have professional experience working with the MERN stack. I also have experience working with HTML, CSS, Bootstrap. I love to improve on my craft regularly.</p>
    </div>
    <dl class="skills-diagram">
  <dt class="skill-5">CSS3</dt>
  <dd>5</dd>
  <dt class="skill-10">JavaScript</dt>
  <dd>10</dd>
  <dt class="skill-3">NodeJS</dt>
  <dd>3</dd>
  <dt class="skill-8">Express JS</dt>
  <dd>8</dd>
  <dt class="skill-4">Angular</dt>
  <dd>4</dd>
  <dt class="skill-6">HTML5</dt>
  <dd>6</dd>
  <dt class="skill-7">MongoDB</dt>
  <dd>7</dd>
  <dt class="skill-9">React JS</dt>
  <dd>9</dd>
  <dt class="skill-2">SQL</dt>
  <dd>2</dd>
</dl>
      
           <ul className="list">
               <li className="list-item"><Link to="/about" style={{color: 'white'}}>ABOUT</Link></li>
               <li className="list-item"><Link to="/experience">EXPERIENCE</Link></li>
               <li className="list-item"><Link to="/contact">CONTACT</Link></li>
               <li className="list-item"><Link to="/work">WORK</Link></li>
               <li className="list-item"><a href={Resume}  download>RESUME</a></li>          
         </ul>
            </div>
        )
    }

}

