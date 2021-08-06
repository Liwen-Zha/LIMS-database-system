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
        <body class="d-flex text-center text-white bg-dark">

        <div class="home-page-config d-flex p-3 mx-auto flex-column">
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

            <div className="content">
                <Route path="/log" component={Log}/>
            </div>

            <footer class="mt-auto text-white-50">
                <p>Cover template for <a href="https://getbootstrap.com/" class="text-white">Bootstrap</a>, by <a
                    href="https://twitter.com/mdo" class="text-white">@mdo</a>.</p>
            </footer>
        </div>

        </body>
        </HashRouter>
        </div>
    );

}

export default App;
