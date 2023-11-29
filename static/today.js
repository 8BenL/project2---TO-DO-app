
function TaskBoard(){
    const [tasksNum, setTasksNum]=React.useState([]);
    React.useEffect(()=>{
        axios.get('/api/tasks_board').then((response)=>{
            setTasksNum(response.data.length)
        })
    },[]
    );
    return <div>Tasks Left<br/>{tasksNum}</div>   
}

function CompletedBoard(){
    const [completedNum, setCompletedNum]=React.useState([]);
    React.useEffect(()=>{
        axios.get('/api/completed_board').then((response)=>{
            setCompletedNum(response.data.length)
        })
    },[]
    );
    return <div>Completed<br/>{completedNum}</div>   
}

function LineThrough(){
    const [completed, setCompleted]=React.useState([]);
    React.useEffect(()=>{
        axios.get('/api/completed').then((response)=>{
            setCompleted(response.data)
        })
    },[]
    );
    return <div>{completed}</div>   
}





const tasks_board = ReactDOM.createRoot(document.getElementById("tasks_board"));
const completed_board = ReactDOM.createRoot(document.getElementById("completed_board"));
tasks_board.render(<TaskBoard/>);
completed_board.render(<CompletedBoard/>);


