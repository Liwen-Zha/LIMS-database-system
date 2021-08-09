import React, {Component} from 'react';
import '../App.css'
import axios from 'axios';

class Log_backup extends Component {
    constructor(props){
        super(props)
        this.state = {
            inputText:"",
            titleText:"Title",
            bodyText:"Here is the body"

        }
    }

    sampleLogWithBackend(){
        const _this=this;    //先存一下this，以防使用箭头函数this会指向我们不希望它所指向的对象。
        axios.get('https://5b5e71c98e9f160014b88cc9.mockapi.io/api/v1/lists')
        .then(function (response) {
            _this.setState({
                users:response.data,
                isLoaded:true
            });
        })
        .catch(function (error) {
            console.log(error);
            _this.setState({
                isLoaded:false,
                error:error
            })
        })
    }

    sampleLogWithBackend2(){
        const _this=this;    //先存一下this，以防使用箭头函数this会指向我们不希望它所指向的对象。
        axios.post('/log',{
            type: _this.state.inputType,
            id: _this.state.inputID,
            loc: _this.state.inputLoc,
            status: _this.state.inputStatus,
            Qvar: _this.state.inputQ,
            Qvar_unit: _this.state.inputUnit,
            custodian: _this.state.inputCustodian


        })
        .then(function (response) {
            _this.setState({
                users:response.data,
                isLoaded:true
            });
        })
        .catch(function (error) {
            console.log(error);
            _this.setState({
                isLoaded:false,
                error:error
            })
        })
    }

    sampleLogWithBackend3(){
        const _this=this;    //先存一下this，以防使用箭头函数this会指向我们不希望它所指向的对象。
        axios.post('/log',{
            sample_type: _this.state.inputType,
            sample_ID: _this.state.inputID,
            loc: _this.state.inputLoc,
            status: _this.state.inputStatus,
            Q: _this.state.inputQ,
            unit: _this.state.inputUnit,
            custodian: _this.state.inputCustodian
        })
        .then(function (response) {
             console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
    }

    render() {
        return (
        <div>
            <body className="d-flex text-left text-white bg-dark">
            <div className="main-page-config d-flex p-3 mx-auto flex-column">
                <h4 className="float-md-start font-monospace">Please log sample transaction：</h4>
                <form>
                    <div className="mb-0">
                        <label htmlFor="inputSampleType" className="Sample Type:">Sample Type:</label>
                        <input type="type" className="form-control" id="inputSampleType" aria-describedby="typeHelp"/>
                            <div id="typeHelp" className="form-text">e.g., blood, DNA, RNA, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputSampleID" className="form-label">Sample ID:</label>
                        <input type="id" className="form-control" id="inputSampleID" aria-describedby="idHelp"/>
                            <div id="idHelp" className="form-text">e.g., blo001, DNA123, RNA024, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputLocation" className="form-label">Storage Location:</label>
                        <input type="loc" className="form-control" id="inputLocation" aria-describedby="locHelp"/>
                            <div id="locHelp" className="form-text">e.g., f1, f5, f10, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputStatus" className="form-label">Status:</label>
                        <input type="status" className="form-control" id="inputStatus" aria-describedby="statusHelp"/>
                            <div id="statusHelp" className="form-text">i.e., available, in use, booked.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputSampleID" className="form-label">Sample ID:</label>
                        <input type="id" className="form-control" id="inputSampleID" aria-describedby="idHelp"/>
                            <div id="idHelp" className="form-text">e.g., blo001, DNA123, RNA024, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputQuantity" className="form-label">Quantity Variation:</label>
                        <input type="q" className="form-control" id="inputQuantity" aria-describedby="qHelp"/>
                            <div id="qHelp" className="form-text">e.g., 10, -5, -1.5, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputUnit" className="form-label">Unit:</label>
                        <input type="unit" className="form-control" id="inputUnit" aria-describedby="unitHelp"/>
                            <div id="unitHelp" className="form-text">e.g., ml, plate, tube, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputCustodian" className="form-label">Custodian:</label>
                        <input type="custodian" className="form-control" id="inputCustodian" aria-describedby="custodianHelp"/>
                            <div id="custodianHelp" className="form-text">e.g., peter, helen, mary, etc.</div>
                    </div>
                    <button type="submit" className="btn btn-primary">Submit</button>
                </form>

            </div>
            </body>
        </div>
    );
  }
}

export default Log;
