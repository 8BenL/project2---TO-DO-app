function ClickCounter(props){
    const [counter, setCounter]=React.useState(props.init);
    const [initialValue, setInitialValue]=React.useState(props.init);
    const [maxValue, setMaxValue]=React.useState(props.max);
    const inputRef=React.useRef(null);
    return (
        <div>
            <button id="myButton" onClick={
                ()=>{
                    setCounter(()=>counter+1)
                    if (counter>=maxValue){
                        setInitialValue(Math.floor(Math.random(initialValue, maxValue-1)*10));
                        setMaxValue(()=>maxValue-1)
                        setCounter(initialValue);
                    }
                }
            }>
            Click Me
            </button>
            <input onChange={()=>setMaxValue(inputRef.current.value)} ref={inputRef}/>
            { counter>=maxValue?<div style={{"backgroundColor":"red"}}>Counter: { counter }</div>:<div>Counter: { counter }</div> }
            <div>Next Initial Value: { initialValue }</div>
            <div>Max Value: { maxValue }</div>
        </div>
    )
}

function CountDown(){
    const [counter, setCounter]=React.useState(100);
    React.useEffect(()=>{
        setInterval(()=>{
            setCounter((counter)=>counter-1);
        }, 0.01)
    }, []);
    return <div>{ counter }</div>
}

//const root=ReactDOM.createRoot(document.getElementById('root'))
//root.render(<ClickCounter max={20} init={Math.floor(Math.random(1,10)*10)}/>)
//root.render(<CountDown/>)










function Counter(props){
    const [counter, setCounter] = React.useState(props.init);
    const [maxValue, setMaxValue] = React.useState(props.max);
    const [initialValue, setInitialValue] = React.useState(props.init);
    const inputRef = React.useRef(null);
    return (
        <div>
            <button id ="button" onClick={()=>{
                setInitialValue(initialValue)
                setCounter(()=>counter+1)
                if (counter == maxValue){
                    setCounter(initialValue)
                    setInitialValue(Math.floor(Math.random()*10))}
                }
            }>Click Me
            </button>
            <input onChange={()=>setMaxValue(inputRef.current.value)} ref={inputRef}/>
            {counter == maxValue ?<div style={{"backgroundColor":"red"}}>Counter : {counter}</div>:<div>Counter: {counter}</div>}
            <div>Max Value: {maxValue}</div>
            <div>Initial Value: {initialValue}</div>
        </div>
    )
}



function DisplayHooks(){
    const [color, setColor] = React.useState();
    const inputRef = React.useRef(null);
    return<> <input type="text" onChange={()=>
        setColor(inputRef.current.value)} ref={inputRef}/>
        <div style={{"backgroundColor":color}}>{color}</div>
    </>
}



//const root=ReactDOM.createRoot(document.getElementById('root'))
//root.render(<Counter init = {Math.floor(Math.random()*10)} max = {20}/>)


const root=ReactDOM.createRoot(document.getElementById('root'))
root.render(<DisplayHooks/>)



