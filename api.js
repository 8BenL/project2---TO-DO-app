
function ShowNumber(props){
    const [number, setNumber]=React.useState(0);
    React.useEffect(()=>{
        axios.get('/number').then((response)=>{
            setNumber(response.data.number)
        })
    },[]
    );
    return <div>{number}</div>
}

function ShowNumbers(props){
    const [numbers, setNumbers]=React.useState([]);
    React.useEffect(()=>{
        axios.get('/numbers').then((response)=>{
            setNumbers(response.data.numbers)
        })
    },[]
    );
    return <div>{numbers}</div>
}


const root=ReactDOM.createRoot(document.getElementById('root'))
root.render(<ShowNumber/>)