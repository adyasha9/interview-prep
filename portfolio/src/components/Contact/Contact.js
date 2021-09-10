import React, { Component } from 'react'
import {Link} from 'react-router-dom';
import './Contact.css';
import Resume from "../../Resume.docx"



export default class Contact extends Component {
    render() {
        return (
            <div className="contact container">
             <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
           <button><img src={require('../../coolicon.png').default} alt="mode" className="coolicon"/></button>
           <h6>GET IN TOUCH <a href="https://github.com/adyasha9" target="_blank" rel="noreferrer"><span className="fa fa-github"></span></a>   <a href="https://www.linkedin.com/in/adyasha-mishra-3b6ba8193/" target="_blank" rel="noreferrer"> <span className="fab fa-linkedin-in"></span></a>
</h6><br/>
<h1> <a href = "mailto: adyasham918@gmail.com">ADYASHAM918@GMAIL.COM</a></h1>
<img src={require('./man.png').default} alt="artemis" className="man"/>


            
     
           

               

               <ul className="list">
               <li className="list-item"><Link to="/about">ABOUT</Link></li>
               <li className="list-item"><Link to="/experience">EXPERIENCE</Link></li>
               <li className="list-item"><Link to="/contact" style={{color: 'white'}}>CONTACT</Link></li>
               <li className="list-item"><Link to="/work">WORK</Link></li>
               <li className="list-item"><a href={Resume}  download>RESUME</a></li>
           </ul>
            </div>
        )
    }
}
