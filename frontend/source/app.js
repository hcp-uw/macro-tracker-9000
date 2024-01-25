import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import HomePage from './screens/Homepage';          // Import HomePage
import CameraScreen from './screens/CameraScreen';
import MealHistoryScreen from './screens/MealHistoryScreen';
import SettingsScreen from './screens/SettingsScreen';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Homepage} />
        <Route path="/camera" component={CameraScreen} />
        <Route path="/meal-history" component={MealHistoryScreen} />
        <Route path="/settings" component={SettingsScreen} />
        {/* You can add more routes here */}
      </Switch>
    </Router>
  );
}

export default App;