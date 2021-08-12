import React, {Component} from 'react';
import Child from './simpleDemo_childComponent'

class Parent extends Component{
    constructor(props){
        super(props)
        this.state = {
            inputText:"none",
            titleText:"Title",
            bodyText:"Here is the body"

        }
    }
   
    onButtonClick = (e) => {
        if (e.target.id ==="mm"){
            this.setState({
                titleText: this.state.inputText
            })    
        } 
        else if(e.target.id ==="body"){
            this.setState({
                bodyText: this.state.inputText
            })
        }   
    }

    handleInput = (e) => {
        this.setState({
            inputText: e.target.value
        })
    }

    render(){
        return(
            <div>
                <div class="container">
                    <div class="row mt-4">
                        <div class="col-sm">
                            <div className="input-group">
                                <input type="text" className="form-control" aria-label="Text input with dropdown button"
                                       onChange={this.handleInput}/>
                                <button className="btn btn-outline-secondary dropdown-toggle" type="button"
                                        data-bs-toggle="dropdown" aria-expanded="false">Dropdown
                                </button>
                                <ul className="dropdown-menu">
                                    <li><button className="dropdown-item" id='mm' onClick={this.onButtonClick}>Title</button></li>
                                    <li><button className="dropdown-item" id='body' onClick={this.onButtonClick}>Body</button></li>
                                </ul>
                            </div>
                        </div>
                        <div className='col-sm'>

                            <Child mm={this.state.titleText} body={this.state.bodyText}/>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

}
//props :pass through (child to parent)
//state :inside (inside parent)
export default Parent
