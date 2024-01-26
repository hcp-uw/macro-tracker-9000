import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import HomePage from './screens/HomePage'; // Correct the file path if necessary
import CameraScreen from './screens/CameraScreen'; // Add the missing semicolon at the end
import MealHistoryScreen from './screens/MealHistoryScreen'; // Add the missing semicolon at the end
import SettingsScreen from './screens/SettingsScreen'; // Add the missing semicolon at the end

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Homepage} /> {/* Use HomePage, the name you imported */}
        <Route path="/camera" component={CameraScreen} />
        <Route path="/meal-history" component={MealHistoryScreen} />
        <Route path="/settings" component={SettingsScreen} />
        {/* You can add more routes here */}
      </Switch>
    </Router>
  );
}

export default App;