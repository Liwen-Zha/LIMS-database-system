import './App.css';
import React from "react";
import Log from "./pages/Log";
import Search from "./pages/Search";
import Check from "./pages/Check";
import View from "./pages/View";
import {
    Route,
    HashRouter
} from "react-router-dom";
import { NavLink } from "react-router-dom";

function App() {
  //console.log("hello")
    return (
        <div class="App">
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

            <Route path="/log" component={Log}/>
            <Route path="/search" component={Search}/>
            <Route path = '/check' component={Check} />
            <Route path = '/view' component={View} />



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
