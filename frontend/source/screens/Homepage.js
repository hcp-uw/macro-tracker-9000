import React from 'react';
import { View, Text, Button, StyleSheet } from 'react';

const HomePage = ({ navigation }) => {
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Welcome to MACRO TRACKER 9000</Text>
            <Text style={styles.subtitle}>Your smart dietary companion</Text>
            <Button 
                title="Start Tracking" 
                onPress={() => navigation.navigate('CameraScreen')}
            />
            <Button 
                title="View Meal History" 
                onPress={() => navigation.navigate('MealHistoryScreen')}
            />
            <Button 
                title="Settings" 
                onPress={() => navigation.navigate('SettingsScreen')}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 10
    },
    subtitle: {
        fontSize: 18,
        marginBottom: 20
    }
});

export default HomePage;