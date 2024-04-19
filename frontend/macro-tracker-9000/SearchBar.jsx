import React, { useState, useEffect } from 'react';
import { Button, View } from 'react-native';

const search = async (query) => {
  return [query];
  return ['search result 1', 'search result 2', 'search result 3'];
  // return await fetch(`https://localhost:80/search/?query=${query}`);
}

const makeCreateMealRequest = async (mealName) => {
  return 21;
  // return await fetch('https://localhost:80/create-meal/?mealName=${mealName}`)
}

export default function SearchBar({ query, navigation }) {
  [searchResults, setSearchResults] = useState([]);
  useEffect(() => {
    (async () => {
      setSearchResults(await search(query));
    })();
  }, [query]);
  const createMeal = async (mealName) => {
    const mealId = await makeCreateMealRequest(mealName);
    navigation.navigate('Meal', { mealId });
  };
  return <View>
    {searchResults.map((result) => <Button key={result} title={result} onPress={() => createMeal(result)}></Button>)}
  </View>;
}