import React, { Component } from 'react'
import './About.css'
import {Link} from 'react-router-dom';
import Resume from "../../Resume.docx"
import { TimelineMax, Power1, Linear } from "gsap/all";

export default class About extends Component {
    constructor(props) {
        super(props);
        this.timeline = new TimelineMax({ paused: true });
      }
      componentDidMount() {
        this.timeline
          .from(this.content, 0.5, {
            display: "none",
            autoAlpha: 0,
            delay: 0.25,
            ease: Power1.easeIn
          })
          .from(this.circle1, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle2, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle3, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle4, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle5, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle6, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle7, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle8, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          })
          .from(this.circle9, 0.3, {
            y: 25,
            autoAlpha: 0,
            ease: Power1.easeInOut
          });
       
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
            <div className="about">           
          <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
           <button><img src={require('../../coolicon.png').default} alt="mode" className="coolicon"/></button>

        
    <img src={require('./artemis.png').default} alt="artemis" className="artemis"/>
    <div className="row" ref={div => (this.content = div)}>
    <p>Hey, I am a full-stack developer completing my BE at <span className="fas fa-graduation-cap"></span> SIES Graduate School Of Technology ,looking forward to getting industry exposure who loves building web applications. I have industry experience building websites and web applications. I specialize in JavaScript and have professional experience working with the MERN stack. I also have experience working with HTML, CSS, Bootstrap. I love to improve on my craft regularly.</p>
    </div>
    <dl class="skills-diagram">
  <dt class="skill-5">CSS3</dt>
  <dd ref={d => (this.circle1 = d)}>5</dd>
  <dt class="skill-10">JavaScript</dt>
  <dd ref={d => (this.circle2 = d)}>10</dd>
  <dt class="skill-3">NodeJS</dt>
  <dd ref={d => (this.circle3 = d)}>3</dd>
  <dt class="skill-8">Express JS</dt>
  <dd ref={d => (this.circle4 = d)}>8</dd>
  <dt class="skill-4">Angular</dt>
  <dd ref={d => (this.circle5 = d)}>4</dd>
  <dt class="skill-6">HTML5</dt>
  <dd ref={d => (this.circle6 = d)}>6</dd>
  <dt class="skill-7">MongoDB</dt>
  <dd ref={d => (this.circle7 = d)}>7</dd>
  <dt class="skill-9">React JS</dt>
  <dd ref={d => (this.circle8 = d)}>9</dd>
  <dt class="skill-2">SQL</dt>
  <dd ref={d => (this.circle9 = d)}>2</dd>
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

