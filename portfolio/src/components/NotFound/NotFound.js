import React, { Component } from 'react'
import HorizontalScroll from 'react-scroll-horizontal'
import Home from '../Home/Home';
import About from '../About/About';
import Contact from '../Contact/Contact';
import Work from '../Work/Work';
import Experience from '../Experience/Experience';
export default class NotFound extends Component {
    render() {
        const child   = { width: `30em`, height: `100%`}
        const parent  = { width: `60em`, height: `100%`}
        return (
            
                   <HorizontalScroll>
                       <div style={parent}>
    <Home style={child}/>
    <About style={child}/>
    <Work style={child}/>
    <Contact style={child}/>
    <Experience style={child}/>
    </div>
    </HorizontalScroll>
                
        )
    }
}
