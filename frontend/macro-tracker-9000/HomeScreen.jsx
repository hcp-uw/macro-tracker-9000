import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { Text, View, Button } from 'react-native';
import { launchCamera } from 'react-native-image-picker';
import { StyleSheet } from 'react-native';
import SearchBar from './SearchBar';

const predict = async (imageBase64) => {
  return ['Fried Frog Legs'];
  // return await fetch(`https://localhost:80/predict/?image=${imageBase64}`);
}

export default function HomeScreen({ navigation }) {
  const [searchQuery, setSearchQuery] = useState("");
  const openCamera = async () => {
    console.log("Pressed");
    // const result = await launchCamera({ mediaType: 'photo', includeBase64: true });
    // if (result.errorCode) {
    //   return;
    // }
    // const imageBase64 = result.assets[0].base64;
    imageBase64 = 'nff28u40134='
    const prediction = await predict(imageBase64);
    console.log(prediction);
    setSearchQuery(prediction[0]);
  }
  return <View style={styles.container}>
    <SearchBar query={searchQuery} navigation={navigation}></SearchBar>
    <Text>MACRO TRACKER 9000</Text>
    <Button onPress={openCamera} title="Take a picture of your meal" />
    <StatusBar style="auto" />
  </View>
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});