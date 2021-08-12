import React, {Component} from 'react';

class Child extends Component{

    render(){
        return(
            <div>
                <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{this.props.mm}</h5>
                    <p class="card-text">{this.props.body}</p>
                </div>
                </div>
            </div>


        )
        
    }
}

export default Child
