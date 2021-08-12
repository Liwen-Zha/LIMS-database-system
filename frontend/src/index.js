import './index.css';
import App from './App';
import Log from './pages/Log'
import Search from './pages/Search'
import Check from './pages/Check';
import View from './pages/View';
import ReactDOM from 'react-dom';
import {
    Route,
    HashRouter,
    Switch
} from "react-router-dom";
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
    <HashRouter>
        <Switch>
            <Route exact path = '/' component={App} />
            <Route path = '/log' component={Log} />
            <Route path = '/search' component={Search} />
            <Route path = '/check' component={Check} />
            <Route path = '/view' component={View} />
        </Switch>
    </HashRouter>,
    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
