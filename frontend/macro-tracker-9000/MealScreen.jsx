import React, { useState, useEffect } from "react"
import { Text } from "react-native"

const getMeal = async (mealId) => {
  // return await fetch(`https://localhost:80/meals/mealId`);
  return {};
}

export default function MealScreen({ navigation, route }) {
  [meal, setMeal] = useState(null); 
  useEffect(() => {
    (async () => {
      setMeal(await getMeal(route.params.mealId));
    })();
  }, [route.params.mealId]);
  return <Text>Meal screen!! {route.params.mealId}</Text>
}