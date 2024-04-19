import React, { useState } from "react";
import { View, TextInput, Button } from "react-native";
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    // const token = await fetch(`https://localhost:80/token?username=${username}&password=${password}`);
    const token = 'jwt_token';
    await AsyncStorage.setItem('token', token);
    navigation.navigate('Home');
  }

  return <View>
    <TextInput value={username} onChangeText={setUsername} />
    <TextInput secureTextEntry={true} value={password} onChangeText={setPassword} />
    <Button title="Login" onPress={login}></Button>
  </View>;
}