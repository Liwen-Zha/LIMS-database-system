import React, {Component} from 'react';
import '../App.css'

class View extends Component {
  render() {
    return (
        <div>
            <body className="d-flex text-center text-white bg-dark">
            <div className="main-page-config d-flex p-3 mx-auto flex-column">
                <h1>This is View page!</h1>
            </div>
            </body>
        </div>
    );
  }
}

export default View;
