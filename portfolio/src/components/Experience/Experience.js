import React, { Component } from 'react'
import {Link} from 'react-router-dom';
import './Experience.css'
import Resume from "../../Resume.docx"

export default class Experience extends Component {
    render() {
        return (
            <div className="experience container">           
            <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
             <button><img src={require('../../coolicon.png').default} alt="mode" className="coolicon"/></button>
  
             <div class="experience-container">

<div class="timeline-block timeline-block-right">
   <div class="marker"></div>
   <div class="timeline-content">
      <h3>Niramai Health Analytix, Remote — Backend developer</h3>
      <span>MAY 2021 - PRESENT</span>
      <ul>
          <li>I work on API creation and integration and database management <br/>according to the client’s needs.</li>
          <li>Error handling, adding new functionality and debugging existing <br/>code using MEAN Stack & maintaining the website.</li>
      </ul>

   </div>
</div>

<div class="timeline-block timeline-block-left">
   <div class="marker"></div>
   <div class="timeline-content">
      <h3>Edunomics Tech Solutions, Remote — Full stack developer </h3>
      <span>NOV 2020 - APR 2021</span>
      <ul>

          <li>I worked to improve and maintain the existing websites using <br/>MERN technology.</li>
          <li>Enriched the current websites and added more appealing features. </li>
          <li>Worked closely with the founder and back-end developer to develop <br/> a strategy and plan website releases.</li>
          <li>Demonstrated the ability to work diligently under pressure to meet<br/> deadlines.</li>
      </ul>
   </div>
</div>

<div class="timeline-block timeline-block-right">
   <div class="marker"></div>
   <div class="timeline-content">
      <h3>Startup Inc, Remote — Frontend developer</h3>
      <span>AUG 2020 - NOV 2020</span>
      <ul>
          <li>Developed various web templates and tested front-end code <br/> in multiple browsers to ensure cross-browser compatibility. </li>
          <li>Leveraged responsive web frameworks to consistently complete <br/> product  deliverables ahead of schedule. Used HTML, CSS, JavaScript,<br/> JQuery and Bootstrap.</li>
      </ul>
   </div>
</div>

</div>

        
             <ul className="list">
                 <li className="list-item"><Link to="/about">ABOUT</Link></li>
                 <li className="list-item"><Link to="/experience" style={{color: 'white'}}>EXPERIENCE</Link></li>
                 <li className="list-item"><Link to="/contact">CONTACT</Link></li>
                 <li className="list-item"><Link to="/work">WORK</Link></li>
                 <li className="list-item"><a href={Resume}  download>RESUME</a></li>          
           </ul>
              </div>
        )
    }
}
