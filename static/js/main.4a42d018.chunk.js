(this.webpackJsonpportfolio=this.webpackJsonpportfolio||[]).push([[0],[,,,,,,,,,,,,,,,,function(e,t,c){"use strict";c.r(t),t.default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC8AAAAtCAYAAAA+7zKnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJ/SURBVHgBxZjdcdswEIR3MnmPS2AJ6SDoIO7A6EDuwEwFiSsQ3YFTQZAKkg6MDpwOFN3YnOEIi/8j9M3gQacDtQIPiyMB4JQYM67LC+LajkBa/Ot53OA6WKS1HT9kLnDzfpFr8JBLyIkX7jAecx5TLqlE/Of3i43EliaeCsYvjGNCmaZozf+7+GwwbuPOJOZZYkz8I4ndYwxfSOwplsxuiazyK8bbpgX3cxpPlc3Pi9gI22T2GF31lNssJPYV+2EQ2qM/DxebkBLvEE402M82LYnNyMBqfuUeY2xzIr/zsvneoqE9WDDGNmcSc8iQEy/CR9gms8dvKCBVNsKEfbtNi3xpspxjSW/jEd5CTds8kNgPFFAiXmC3UMM2Dd4avy0e4RlDKRXvwDeuQR+WxGYUUipeYBv3gHYm8GeF3yikRrzU4eXq36J947I/viDSQTJqxLN+R2i1zVsSe0QFHyPxORL/RGIH1L9lsAj7GHcef1HJSWHUOs8fco27RL5Fo8+XUFM6Btwen1BJrGw80kwIBclwyGNJzKGRXHvAmMGfeHJMkd+bMvMsFMtmIbES2+y2xy2t4j14v5OrfWaP1bW+paVsBAPebcawSD9woHJul9s4hCeurL6J5LOSmdFBr1WyE/GBxAxCe5Q/XtzHMHrFs37HIFx9S+Y+o3GjrvSKj/U72405gZ+eRY95KTRO2IXEROxqm6zWHTpXXdAQ75C2TWaPCxTQ6m1Y6ciKW/C3YF3evqIlfgG3ze8kt6pnT6ElPvZ+h7ULz1BCS7ywFOZ4KKEp3iPf2qrU+oqmeCHl3R4dfTtDW7xDuHFXZiijLV5gG9dDuWSEPcSzfsdhB/4D7wMSLVnthk4AAAAASUVORK5CYII="},function(e,t,c){"use strict";c.r(t),t.default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAcCAYAAAAX4C3rAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABfSURBVHgB7dfRDYAwCIThw3QiWKhOpgsxE+oMXpOS3DfBPfEHwwIRUSA70ISGsg2scUNE5Bdz94kGhpldaEAJZevT+qo6ISKyHXtfW3pCM5N+8r6faYKPPlQJZWsz9AFBGAwVNQZ48QAAAABJRU5ErkJggg=="},function(e,t){function c(e){localStorage.setItem("theme",e),document.documentElement.className=e}e.exports={setTheme:c,keepTheme:function(){localStorage.getItem("theme")?"theme-dark"===localStorage.getItem("theme")?c("theme-dark"):"theme-light"===localStorage.getItem("theme")&&c("theme-light"):c("theme-dark")}}},,,,,,,,,,,,,,,,,function(e,t,c){},function(e,t,c){},,,,,,function(e,t,c){"use strict";c.r(t),t.default=c.p+"static/media/women.bc03c3d1.png"},function(e,t,c){},function(e,t,c){"use strict";c.r(t),t.default=c.p+"static/media/artemis.51d35582.png"},function(e,t,c){},function(e,t,c){"use strict";c.r(t),t.default=c.p+"static/media/man.e064e0e0.png"},function(e,t,c){},function(e,t,c){},,function(e,t,c){},function(e,t,c){"use strict";c.r(t);var s=c(2),i=c.n(s),l=c(14),n=c.n(l),a=(c(35),c(9)),r=c(10),j=c(19),o=c(12),d=c(11),b=c(3),h=(c(36),c.p+"static/media/Resume.682e2985.docx"),O=c(29),x=c(18),m=c(0);var u=function(){var e=Object(s.useState)("dark"),t=Object(O.a)(e,2),c=t[0],i=t[1],l=localStorage.getItem("theme"),n=function(){"theme-dark"===localStorage.getItem("theme")?(Object(x.setTheme)("theme-light"),i("light")):(Object(x.setTheme)("theme-dark"),i("dark"))};return Object(s.useEffect)((function(){"theme-dark"===localStorage.getItem("theme")?i("dark"):"theme-light"===localStorage.getItem("theme")&&i("light")}),[l]),Object(m.jsxs)("div",{className:"container--toggle",children:["light"===c?Object(m.jsx)("input",{type:"checkbox",id:"toggle",className:"toggle--checkbox",onClick:n,checked:!0}):Object(m.jsx)("input",{type:"checkbox",id:"toggle",className:"toggle--checkbox",onClick:n}),Object(m.jsx)("label",{htmlFor:"toggle",className:"toggle--label",children:Object(m.jsx)("span",{className:"toggle--label-background"})})]})},f=c(1),p=function(e){Object(o.a)(s,e);var t=Object(d.a)(s);function s(e){var c;return Object(a.a)(this,s),(c=t.call(this,e)).changePage=function(e,t){e.preventDefault(),c.timeline.reverse();var s=1e3*c.timeline.duration();setTimeout((function(){c.props.history.push(t)}),s)},c.timeline=new f.d({paused:!0}),c.state={flag:!1},c.darkmode=c.darkmode.bind(Object(j.a)(c)),c}return Object(r.a)(s,[{key:"darkmode",value:function(){console.log("you have entered into the dark mode"),this.setState({flag:!0})}},{key:"componentDidMount",value:function(){this.timeline.from(this.header,.5,{display:"none",autoAlpha:0,delay:.25,ease:f.b.easeIn}).from(this.content,.4,{autoAlpha:0,y:25,ease:f.b.easeInOut}),this.timeline.play()}},{key:"render",value:function(){var e=this;return Object(m.jsxs)("div",{className:"container home",children:[Object(m.jsxs)("table",{ref:function(t){return e.header=t},children:[Object(m.jsxs)("tr",{children:[Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{}),Object(m.jsx)("th",{})]}),Object(m.jsx)("tr",{children:Object(m.jsx)("td",{})}),Object(m.jsx)("tr",{children:Object(m.jsx)("td",{})}),Object(m.jsxs)("tr",{children:[Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{})]}),Object(m.jsxs)("tr",{children:[Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)("td",{}),Object(m.jsx)(u,{})]})]}),Object(m.jsxs)(b.b,{to:"/",children:[" ",Object(m.jsx)("img",{src:c(16).default,alt:"logo",className:"logo"})]}),Object(m.jsx)("button",{onClick:this.darkmode,children:Object(m.jsx)("img",{src:c(17).default,alt:"mode",className:"coolicon"})}),Object(m.jsxs)("div",{ref:function(t){return e.content=t},children:[Object(m.jsx)("h1",{className:"h1",children:"ADYASHA MISHRA"}),Object(m.jsx)("h6",{style:{color:"rgb(151, 104, 175)"},className:"h6",children:"FULL STACK DEVELOPER"}),Object(m.jsx)("img",{src:c(42).default,alt:"women",className:"women"})]}),Object(m.jsxs)("ul",{className:"list",children:[Object(m.jsx)("li",{className:"list-item",onClick:function(t){return e.changePage(t,"/about")},children:"ABOUT"}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/experience",children:"EXPERIENCE"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/contact",children:"CONTACT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/work",children:"WORK"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)("a",{href:h,download:!0,children:"RESUME"})})]})]})}}]),s}(s.Component),g=(c(43),function(e){Object(o.a)(s,e);var t=Object(d.a)(s);function s(e){var c;return Object(a.a)(this,s),(c=t.call(this,e)).changePage=function(e,t){e.preventDefault(),c.timeline.reverse();var s=1e3*c.timeline.duration();setTimeout((function(){c.props.history.push(t)}),s)},c.timeline=new f.d({paused:!0}),c}return Object(r.a)(s,[{key:"componentDidMount",value:function(){this.timeline.from(this.content,.5,{display:"none",autoAlpha:0,delay:.25,ease:f.b.easeIn}).from(this.circle1,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle2,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle3,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle4,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle5,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle6,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle7,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle8,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}).from(this.circle9,.3,{y:25,autoAlpha:0,ease:f.b.easeInOut}),this.timeline.play()}},{key:"render",value:function(){var e=this;return Object(m.jsxs)("div",{className:"about",children:[Object(m.jsxs)(b.b,{to:"/",children:[" ",Object(m.jsx)("img",{src:c(16).default,alt:"logo",className:"logo"})]}),Object(m.jsx)("button",{children:Object(m.jsx)("img",{src:c(17).default,alt:"mode",className:"coolicon"})}),Object(m.jsx)("img",{src:c(44).default,alt:"artemis",className:"artemis"}),Object(m.jsx)("div",{className:"row",ref:function(t){return e.content=t},children:Object(m.jsxs)("p",{children:["Hey, I am a full-stack developer completing my BE at ",Object(m.jsx)("span",{className:"fas fa-graduation-cap"})," SIES Graduate School Of Technology ,looking forward to getting industry exposure who loves building web applications. I have industry experience building websites and web applications. I specialize in JavaScript and have professional experience working with the MERN stack. I also have experience working with HTML, CSS, Bootstrap. I love to improve on my craft regularly."]})}),Object(m.jsxs)("dl",{class:"skills-diagram",children:[Object(m.jsx)("dt",{class:"skill-5",children:"CSS3"}),Object(m.jsx)("dd",{ref:function(t){return e.circle1=t},children:"5"}),Object(m.jsx)("dt",{class:"skill-10",children:"JavaScript"}),Object(m.jsx)("dd",{ref:function(t){return e.circle2=t},children:"10"}),Object(m.jsx)("dt",{class:"skill-3",children:"NodeJS"}),Object(m.jsx)("dd",{ref:function(t){return e.circle3=t},children:"3"}),Object(m.jsx)("dt",{class:"skill-8",children:"Express JS"}),Object(m.jsx)("dd",{ref:function(t){return e.circle4=t},children:"8"}),Object(m.jsx)("dt",{class:"skill-4",children:"Angular"}),Object(m.jsx)("dd",{ref:function(t){return e.circle5=t},children:"4"}),Object(m.jsx)("dt",{class:"skill-6",children:"HTML5"}),Object(m.jsx)("dd",{ref:function(t){return e.circle6=t},children:"6"}),Object(m.jsx)("dt",{class:"skill-7",children:"MongoDB"}),Object(m.jsx)("dd",{ref:function(t){return e.circle7=t},children:"7"}),Object(m.jsx)("dt",{class:"skill-9",children:"React JS"}),Object(m.jsx)("dd",{ref:function(t){return e.circle8=t},children:"9"}),Object(m.jsx)("dt",{class:"skill-2",children:"SQL"}),Object(m.jsx)("dd",{ref:function(t){return e.circle9=t},children:"2"})]}),Object(m.jsxs)("ul",{className:"list",children:[Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/about",style:{color:"white"},children:"ABOUT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/experience",children:"EXPERIENCE"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/contact",children:"CONTACT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/work",children:"WORK"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)("a",{href:h,download:!0,children:"RESUME"})})]})]})}}]),s}(s.Component)),A=(c(45),function(e){Object(o.a)(s,e);var t=Object(d.a)(s);function s(){return Object(a.a)(this,s),t.apply(this,arguments)}return Object(r.a)(s,[{key:"render",value:function(){return Object(m.jsxs)("div",{className:"contact container",children:[Object(m.jsxs)(b.b,{to:"/",children:[" ",Object(m.jsx)("img",{src:c(16).default,alt:"logo",className:"logo"})]}),Object(m.jsx)("button",{children:Object(m.jsx)("img",{src:c(17).default,alt:"mode",className:"coolicon"})}),Object(m.jsxs)("h6",{children:["GET IN TOUCH ",Object(m.jsx)("a",{href:"https://github.com/adyasha9",target:"_blank",rel:"noreferrer",children:Object(m.jsx)("span",{className:"fa fa-github"})}),"   ",Object(m.jsxs)("a",{href:"https://www.linkedin.com/in/adyasha-mishra-3b6ba8193/",target:"_blank",rel:"noreferrer",children:[" ",Object(m.jsx)("span",{className:"fab fa-linkedin-in"})]})]}),Object(m.jsx)("br",{}),Object(m.jsxs)("h1",{children:[" ",Object(m.jsx)("a",{href:"mailto: adyasham918@gmail.com",children:"ADYASHAM918@GMAIL.COM"})]}),Object(m.jsx)("img",{src:c(46).default,alt:"artemis",className:"man"}),Object(m.jsxs)("ul",{className:"list",children:[Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/about",children:"ABOUT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/experience",children:"EXPERIENCE"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/contact",style:{color:"white"},children:"CONTACT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/work",children:"WORK"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)("a",{href:h,download:!0,children:"RESUME"})})]})]})}}]),s}(s.Component)),v=(c(47),function(e){Object(o.a)(s,e);var t=Object(d.a)(s);function s(e){var c;return Object(a.a)(this,s),(c=t.call(this,e)).changePage=function(e,t){e.preventDefault(),c.timeline.reverse();var s=1e3*c.timeline.duration();setTimeout((function(){c.props.history.push(t)}),s)},c.timeline=new f.d({paused:!0}),c}return Object(r.a)(s,[{key:"componentDidMount",value:function(){this.timeline.from(this.content,.4,{autoAlpha:0,y:25,ease:f.b.easeInOut}),this.timeline.play()}},{key:"render",value:function(){var e=this;return Object(m.jsxs)("div",{className:"container work",children:[Object(m.jsxs)(b.b,{to:"/",children:[" ",Object(m.jsx)("img",{src:c(16).default,alt:"logo",className:"logo"})]}),Object(m.jsx)("button",{children:Object(m.jsx)("img",{src:c(17).default,alt:"mode",className:"coolicon"})}),Object(m.jsxs)("div",{class:"cardcontainer",ref:function(t){return e.content=t},children:[Object(m.jsxs)("div",{class:"card",children:[Object(m.jsx)("h3",{class:"title",children:"Telegram Clone"}),Object(m.jsxs)("div",{class:"bar",children:[Object(m.jsx)("div",{class:"emptybar"}),Object(m.jsx)("div",{class:"filledbar"})]}),Object(m.jsx)("div",{class:"circle",children:Object(m.jsxs)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",children:[Object(m.jsx)("circle",{class:"stroke",cx:"60",cy:"60",r:"50"}),Object(m.jsx)("text",{x:"60",y:"60","text-anchor":"middle",fill:"white","font-size":"20px","font-family":"Arya",dy:".3em",children:Object(m.jsx)("a",{href:"https://github.com/adyasha9/telegram-clone",target:"_blank",rel:"noreferrer",children:"Link"})})]})})]}),Object(m.jsxs)("div",{class:"card",children:[Object(m.jsx)("h3",{class:"title",children:"React Movie Search Website"}),Object(m.jsxs)("div",{class:"bar",children:[Object(m.jsx)("div",{class:"emptybar"}),Object(m.jsx)("div",{class:"filledbar"})]}),Object(m.jsx)("div",{class:"circle",children:Object(m.jsxs)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",children:[Object(m.jsx)("circle",{class:"stroke",cx:"60",cy:"60",r:"50"}),Object(m.jsx)("text",{x:"60",y:"60","text-anchor":"middle",fill:"white","font-size":"20px","font-family":"Arya",dy:".3em",children:Object(m.jsx)("a",{href:"https://github.com/adyasha9/react-movie-search-app",target:"_blank",rel:"noreferrer",children:"Link"})})]})})]}),Object(m.jsxs)("div",{class:"card",children:[Object(m.jsx)("h3",{class:"title",children:"MERN E-COMMERCE"}),Object(m.jsxs)("div",{class:"bar",children:[Object(m.jsx)("div",{class:"emptybar"}),Object(m.jsx)("div",{class:"filledbar"})]}),Object(m.jsx)("div",{class:"circle",children:Object(m.jsxs)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",children:[Object(m.jsx)("circle",{class:"stroke",cx:"60",cy:"60",r:"50"}),Object(m.jsx)("text",{x:"60",y:"60","text-anchor":"middle",fill:"white","font-size":"20px","font-family":"Arya",dy:".3em",children:Object(m.jsx)("a",{href:"https://github.com/adyasha9/react-shop/tree/master/shop",target:"_blank",rel:"noreferrer",children:"Link"})})]})})]}),Object(m.jsxs)("div",{class:"card",children:[Object(m.jsx)("h3",{class:"title",children:"Intent Recognition Chatbot"}),Object(m.jsxs)("div",{class:"bar",children:[Object(m.jsx)("div",{class:"emptybar"}),Object(m.jsx)("div",{class:"filledbar"})]}),Object(m.jsx)("div",{class:"circle",children:Object(m.jsxs)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",children:[Object(m.jsx)("circle",{class:"stroke",cx:"60",cy:"60",r:"50"}),Object(m.jsx)("text",{x:"60",y:"60","text-anchor":"middle",fill:"white","font-size":"20px","font-family":"Arya",dy:".3em",children:"Link"})]})})]}),Object(m.jsxs)("div",{class:"card",style:{background:"rgb(151,104,175)"},children:[Object(m.jsx)("h3",{class:"title",children:"RDC Concrete Website"}),Object(m.jsxs)("div",{class:"bar",children:[Object(m.jsx)("div",{class:"emptybar"}),Object(m.jsx)("div",{class:"filledbar"})]}),Object(m.jsx)("div",{class:"circle",children:Object(m.jsxs)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",children:[Object(m.jsx)("circle",{class:"stroke",cx:"60",cy:"60",r:"50"}),Object(m.jsx)("text",{x:"60",y:"60","text-anchor":"middle",fill:"white","font-size":"20px","font-family":"Arya",dy:".3em",children:Object(m.jsx)("a",{href:"http://qms.rdcconcrete.com/#/",target:"_blank",rel:"noreferrer",children:"Link"})})]})})]}),Object(m.jsxs)("div",{class:"card",style:{background:"rgb(151,104,175)"},children:[Object(m.jsx)("h3",{class:"title",children:"Medical Booking Website"}),Object(m.jsxs)("div",{class:"bar",children:[Object(m.jsx)("div",{class:"emptybar"}),Object(m.jsx)("div",{class:"filledbar"})]}),Object(m.jsx)("div",{class:"circle",children:Object(m.jsxs)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",children:[Object(m.jsx)("circle",{class:"stroke",cx:"60",cy:"60",r:"50"}),Object(m.jsx)("text",{x:"60",y:"60","text-anchor":"middle",fill:"white","font-size":"20px","font-family":"Arya",dy:".3em",children:Object(m.jsx)("a",{href:"https://qahs.thermalytix.com/",target:"_blank",rel:"noreferrer",children:"Link"})})]})})]})]}),Object(m.jsxs)("ul",{className:"worklist",children:[Object(m.jsxs)("li",{className:"work-item",children:[" ",Object(m.jsx)("span",{className:"dot",style:{background:"rgb(151,104,175)"}})," Intership Project"]}),Object(m.jsxs)("li",{className:"work-item",children:[" ",Object(m.jsx)("span",{className:"dot"})," Personal Project"]})]}),Object(m.jsxs)("ul",{className:"list",children:[Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/about",children:"ABOUT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/experience",children:"EXPERIENCE"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/contact",children:"CONTACT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/work",style:{color:"white"},children:"WORK"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)("a",{href:h,download:!0,children:"RESUME"})})]})]})}}]),s}(s.Component)),y=(c(48),function(e){Object(o.a)(s,e);var t=Object(d.a)(s);function s(){return Object(a.a)(this,s),t.apply(this,arguments)}return Object(r.a)(s,[{key:"render",value:function(){return Object(m.jsxs)("div",{className:"experience container",children:[Object(m.jsxs)(b.b,{to:"/",children:[" ",Object(m.jsx)("img",{src:c(16).default,alt:"logo",className:"logo"})]}),Object(m.jsx)("button",{children:Object(m.jsx)("img",{src:c(17).default,alt:"mode",className:"coolicon"})}),Object(m.jsxs)("div",{class:"experience-container",children:[Object(m.jsxs)("div",{class:"timeline-block timeline-block-right",children:[Object(m.jsx)("div",{class:"marker"}),Object(m.jsxs)("div",{class:"timeline-content",children:[Object(m.jsx)("h3",{children:"Niramai Health Analytix, Remote \u2014 Backend developer"}),Object(m.jsx)("span",{children:"MAY 2021 - PRESENT"}),Object(m.jsxs)("ul",{children:[Object(m.jsxs)("li",{children:["I work on API creation and integration and database management ",Object(m.jsx)("br",{}),"according to the client\u2019s needs."]}),Object(m.jsxs)("li",{children:["Error handling, adding new functionality and debugging existing ",Object(m.jsx)("br",{}),"code using MEAN Stack & maintaining the website."]})]})]})]}),Object(m.jsxs)("div",{class:"timeline-block timeline-block-left",children:[Object(m.jsx)("div",{class:"marker"}),Object(m.jsxs)("div",{class:"timeline-content",children:[Object(m.jsx)("h3",{children:"Edunomics Tech Solutions, Remote \u2014 Full stack developer "}),Object(m.jsx)("span",{children:"NOV 2020 - APR 2021"}),Object(m.jsxs)("ul",{children:[Object(m.jsxs)("li",{children:["I worked to improve and maintain the existing websites using ",Object(m.jsx)("br",{}),"MERN technology."]}),Object(m.jsx)("li",{children:"Enriched the current websites and added more appealing features. "}),Object(m.jsxs)("li",{children:["Worked closely with the founder and back-end developer to develop ",Object(m.jsx)("br",{})," a strategy and plan website releases."]}),Object(m.jsxs)("li",{children:["Demonstrated the ability to work diligently under pressure to meet",Object(m.jsx)("br",{})," deadlines."]})]})]})]}),Object(m.jsxs)("div",{class:"timeline-block timeline-block-right",children:[Object(m.jsx)("div",{class:"marker"}),Object(m.jsxs)("div",{class:"timeline-content",children:[Object(m.jsx)("h3",{children:"Startup Inc, Remote \u2014 Frontend developer"}),Object(m.jsx)("span",{children:"AUG 2020 - NOV 2020"}),Object(m.jsxs)("ul",{children:[Object(m.jsxs)("li",{children:["Developed various web templates and tested front-end code ",Object(m.jsx)("br",{})," in multiple browsers to ensure cross-browser compatibility. "]}),Object(m.jsxs)("li",{children:["Leveraged responsive web frameworks to consistently complete ",Object(m.jsx)("br",{})," product  deliverables ahead of schedule. Used HTML, CSS, JavaScript,",Object(m.jsx)("br",{})," JQuery and Bootstrap."]})]})]})]})]}),Object(m.jsxs)("ul",{className:"list",children:[Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/about",children:"ABOUT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/experience",style:{color:"white"},children:"EXPERIENCE"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/contact",children:"CONTACT"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)(b.b,{to:"/work",children:"WORK"})}),Object(m.jsx)("li",{className:"list-item",children:Object(m.jsx)("a",{href:h,download:!0,children:"RESUME"})})]})]})}}]),s}(s.Component)),k=c(28),w=function(e){Object(o.a)(c,e);var t=Object(d.a)(c);function c(){return Object(a.a)(this,c),t.apply(this,arguments)}return Object(r.a)(c,[{key:"render",value:function(){var e={width:"30em",height:"100%"};return Object(m.jsx)(k.a,{children:Object(m.jsxs)("div",{style:{width:"60em",height:"100%"},children:[Object(m.jsx)(p,{style:e}),Object(m.jsx)(g,{style:e}),Object(m.jsx)(v,{style:e}),Object(m.jsx)(A,{style:e}),Object(m.jsx)(y,{style:e})]})})}}]),c}(s.Component),N=c(4),E=(c(50),c(30));var S=function(){var e=E.a.timeline();return Object(s.useEffect)((function(){Object(x.keepTheme)()})),Object(m.jsx)("div",{className:"App",children:Object(m.jsxs)(b.a,{children:[Object(m.jsx)(N.a,{exact:!0,path:"/",component:p,timeline:e}),Object(m.jsx)(N.a,{path:"/about",component:g}),Object(m.jsx)(N.a,{path:"/work",component:v}),Object(m.jsx)(N.a,{path:"/contact",component:A}),Object(m.jsx)(N.a,{path:"/experience",component:y}),Object(m.jsx)(N.a,{path:"/NotFound",component:w})]})})},I=function(e){e&&e instanceof Function&&c.e(3).then(c.bind(null,52)).then((function(t){var c=t.getCLS,s=t.getFID,i=t.getFCP,l=t.getLCP,n=t.getTTFB;c(e),s(e),i(e),l(e),n(e)}))};n.a.render(Object(m.jsx)(i.a.StrictMode,{children:Object(m.jsx)(S,{})}),document.getElementById("root")),I()}],[[51,1,2]]]);
//# sourceMappingURL=main.4a42d018.chunk.js.map