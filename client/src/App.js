import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      widgets: null,
    };
  }

  componentDidMount() {
    fetch('http://localhost:8080/rest/widgets/all')
        .then(response => response.json())
        .then((responseJson) => {
          console.log('responseJson', responseJson)
          this.setState({
            widgets: responseJson,
          });
        });
  }

  render() {
    const { widgets } = this.state;
    return (
      <div>
        <h1>Widgets</h1>
        <ul>
          {
            widgets
            ? widgets.map((w) => {return <li key={w.name}>{w.name} - <em>{w.age}</em></li>})
            : null
          }
        </ul>
      </div>
    );
  }
}

export default App;
