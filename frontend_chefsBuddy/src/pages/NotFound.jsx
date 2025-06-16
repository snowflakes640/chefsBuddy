import { Link } from "react-router-dom";

const NotFound = () => {
    return ( 
        <div>
            <h2>Sorry</h2>
            <h5>but not sorry</h5>
            <p>error 404: page cannot be found</p>
            <Link to="/">Back to homepage</Link>
        </div>
     );
}
 
export default NotFound;