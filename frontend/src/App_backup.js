import './App.css';
import React from "react";
import Log from "./pages/Log.jsx";
import {
    Route,
    HashRouter
} from "react-router-dom";
import { NavLink } from "react-router-dom";

function App() {
  //console.log("hello")
    return (
        <div>
        <HashRouter>

        <body class="text-center text-white bg-dark">

        <div class="main-page-config d-flex p-3 mx-auto flex-column">
            <header class="mb-auto">
                <div>
                    <h5 class="float-md-start font-monospace">Prof Kitney's Lab</h5>
                    <nav class="nav nav-masthead justify-content-center float-md-end">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                        <a class="nav-link" href="https://www.imperial.ac.uk/synthetic-biology">Contact</a>
                    </nav>
                </div>
            </header>

            <main class="px-4">
                <h1 float-sm-start>Laboratory Inventory Management System (LIMS)</h1>
                <p class="lead">LIMS is designed to track and organize the samples in the lab, considered as one of
                    the most efficient platforms for experimental data recording and management.</p>
                <p class="lead">
                    <div className="container">
                        <div className="row g-1">
                            <div className="col-3">
                                <NavLink to='/log'>
                                    <button class="btn btn-outline-primary btn-lg" type="button">Log</button>
                                </NavLink>
                            </div>
                            <div className="col-3">
                                <NavLink to='/search'>
                                    <button className="btn btn-outline-secondary btn-lg" type="button">Search</button>
                                </NavLink>
                            </div>
                            <div className="col-3">
                                 <NavLink to='/check'>
                                     <button className="btn btn-outline-success btn-lg" type="button">Check</button>
                                 </NavLink>
                            </div>
                            <div className="col-3">
                                <NavLink to='/view'>
                                    <button className="btn btn-outline-danger btn-lg" type="button">View</button>
                                </NavLink>
                            </div>
                        </div>
                    </div>
                </p>
            </main>

            <Route exact path="/log" component={Log}/>



            <footer class="mt-auto text-white-50">
                <p>Home page from<a href="https://getbootstrap.com/" class="text-white">Bootstrap</a>, by <a
                    href="https://www.imperial.ac.uk" class="text-white">@imperial</a>.</p>
            </footer>
        </div>

        </body>
        </HashRouter>
        </div>
    );

}
export default App;


/*
zoom in page
did not know why
*/
import './App.css';
import React from "react";

function App() {
  //console.log("hello")
    return (
        <body>

        <main>
            <h1 className="visually-hidden">Heroes examples</h1>

            <div className="px-4 py-5 my-5 text-center text-white bg-dark">

                    <h1 className="display-5 fw-bold">Centered hero</h1>
                    <div className="col-lg-6 mx-auto">
                        <p className="lead mb-4">Quickly design and customize responsive mobile-first sites with
                            Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables
                            and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript
                            plugins.</p>
                        <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
                            <button type="button" className="btn btn-primary btn-lg px-4 gap-3">Primary button</button>
                            <button type="button" className="btn btn-outline-secondary btn-lg px-4">Secondary</button>
                        </div>
                    </div>
            </div>
        </main>
        </body>
    );

}

export default App;

