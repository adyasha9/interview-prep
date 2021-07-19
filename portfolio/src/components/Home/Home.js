import React, { Component } from 'react'
import './Home.css'
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
export default class Home extends Component {
    render() {
        return (
            <div className="container">
                <div className="circle">
              <p>GET IN <br/>TOUCH</p> 
           </div>
           <h5>PORTFOLIO OF ADYASHA MISHRA</h5>
           <h1>ADYASHA <br/>MISHRA</h1>
          
           
           <ul>
               <li>ABOUT</li>
               <li>CONTACT</li>
               <li>WORK</li>
               <li>RESUME</li>
           </ul>
           <ArrowDownwardIcon/>
            </div>
        )
    }
}

