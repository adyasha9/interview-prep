import React, { Component } from 'react'
import './Work.css'
import {Link} from 'react-router-dom';
import Resume from "../../Resume.docx"

export default class Work extends Component {
      
    render() {    
       
        return (
            <div className="container work">           
          <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
           <button><img src={require('../../coolicon.png').default} alt="mode" className="coolicon"/></button>
        <div class="cardcontainer">
  <div class="card">
    <h3 class="title">Telegram Clone</h3>
    <div class="bar">
      <div class="emptybar"></div>
      <div class="filledbar"></div>
    </div>
   <div class="circle">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      <circle class="stroke" cx="60" cy="60" r="50"/>
      <text x="60" y="60" text-anchor="middle" fill="white" font-size="20px" font-family="Arya" dy=".3em"><a href="https://github.com/adyasha9/telegram-clone" target="_blank" rel="noreferrer">Link</a></text>

    </svg>
    </div>
  </div>
  <div class="card">
    <h3 class="title">React Movie Search Website</h3>
    <div class="bar">
      <div class="emptybar"></div>
      <div class="filledbar"></div>
    </div>
    <div class="circle">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      <circle class="stroke" cx="60" cy="60" r="50"/>
      <text x="60" y="60" text-anchor="middle" fill="white" font-size="20px" font-family="Arya" dy=".3em"><a href="https://github.com/adyasha9/react-movie-search-app" target="_blank" rel="noreferrer">Link</a></text>

    </svg>
    </div>
  </div>
  <div class="card">
    <h3 class="title">MERN E-COMMERCE</h3>
    <div class="bar">
      <div class="emptybar"></div>
      <div class="filledbar"></div>
    </div>
    <div class="circle">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      <circle class="stroke" cx="60" cy="60" r="50"/>
      <text x="60" y="60" text-anchor="middle" fill="white" font-size="20px" font-family="Arya" dy=".3em"><a href="https://github.com/adyasha9/react-shop/tree/master/shop" target="_blank" rel="noreferrer">Link</a></text>

    </svg>
    </div>
  </div>
  <div class="card">
    <h3 class="title">Intent Recognition Chatbot</h3> 
    <div class="bar">
      <div class="emptybar"></div>
      <div class="filledbar"></div>
    </div>
    <div class="circle">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      <circle class="stroke" cx="60" cy="60" r="50"/>
      <text x="60" y="60" text-anchor="middle" fill="white" font-size="20px" font-family="Arya" dy=".3em">Link</text>

    </svg>
    </div>
  </div>
  <div class="card" style={{background:'rgb(151,104,175)'}}>
    <h3 class="title">RDC Concrete Website</h3>
    <div class="bar">
      <div class="emptybar"></div>
      <div class="filledbar"></div>
    </div>
    <div class="circle">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
      <circle class="stroke" cx="60" cy="60" r="50"/>
      <text x="60" y="60" text-anchor="middle" fill="white" font-size="20px" font-family="Arya" dy=".3em"><a href="http://qms.rdcconcrete.com/#/" target="_blank" rel="noreferrer">Link</a></text>
    </svg>
    </div>
  </div>

  <div class="card" style={{background:'rgb(151,104,175)'}}>
    <h3 class="title">Medical Booking Website</h3>
    <div class="bar">
      <div class="emptybar"></div>
      <div class="filledbar"></div>
    </div>
    
    <div class="circle">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
          
      <circle class="stroke" cx="60" cy="60" r="50"/>
      <text x="60" y="60" text-anchor="middle" fill="white" font-size="20px" font-family="Arya" dy=".3em"><a href="https://qahs.thermalytix.com/" target="_blank" rel="noreferrer">Link</a></text>
     
    </svg>
    </div>
  </div>
  
</div>

<ul className="worklist">
<li className="work-item"> <span className="dot" style={{background:'rgb(151,104,175)'}}></span> Intership Project</li>

<li className="work-item"> <span className="dot"></span> Personal Project</li>
</ul>

          
      
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

