import React, { Component } from 'react'
import {Link} from 'react-router-dom';
import './Home.css'
import Resume from "../../Resume.docx"
export default class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {
            flag: false,
        };
        this.darkmode = this.darkmode.bind(this);
      }
      
      darkmode() {
        console.log('you have entered into the dark mode');
        this.setState({ flag: true });
      }
      
    render() {    
       
        return (
            <div className="container home">  
            <table>
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
  </tr>
  
 
</table>         
           <h1>ADYASHA MISHRA</h1>
           <Link to="/"> <img src={require('../../Vector.png').default} alt="logo" className="logo" /></Link>
           <button onClick={this.darkmode}><img src={require('../../coolicon.png').default} alt="mode" className="coolicon" /></button>

           <h6>FULL STACK DEVELOPER</h6>
           <img src={require('./women.png').default} alt="women" className="women"/> 
          
           
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

