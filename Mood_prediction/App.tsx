import React, { useState } from 'react';
import { StyleSheet, Text, TextInput, View, TouchableOpacity, ActivityIndicator, ScrollView, Animated, Easing, SafeAreaView } from 'react-native';
import Feather from 'react-native-vector-icons/Feather';

const App = () => {
  const [text, setText] = useState('');
  const [moods, setMoods] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [fadeAnim] = useState(new Animated.Value(0));

  const predictMood = async () => {
    if (!text.trim()) {
      setError('Please enter some text');
      return;
    }
    setLoading(true);
    setError('');
    try {
      const response = await fetch('http://10.0.2.2:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ lyrics: text }),
      });
      const data = await response.json();
      console.log('Response from server:', data);
      
      if (data.predictedMoods && Array.isArray(data.predictedMoods)) {
        setMoods(data.predictedMoods);
        fadeIn(); // Trigger fade-in animation
      } else {
        setError('No moods predicted');
        setMoods([]);
      }
    } catch (error) {
      console.error(error);
      setError('An error occurred. Please try again.');
      setMoods([]);
    } finally {
      setLoading(false);
    }
  };

  // Fade-in animation function
  const fadeIn = () => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 500,
      easing: Easing.ease,
      useNativeDriver: true,
    }).start();
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title}>Mood Predictor</Text>
        <TextInput
          style={styles.textInput}
          placeholder="Enter lyrics here..."
          placeholderTextColor="#888"
          value={text}
          onChangeText={setText}
          multiline
        />
        <TouchableOpacity style={styles.button} onPress={predictMood} disabled={loading}>
          {loading ? (
            <ActivityIndicator color="#fff" size="large" />
          ) : (
            <Text style={styles.buttonText}>Predict Mood</Text>
          )}
        </TouchableOpacity>
        {error ? <Text style={styles.errorText}>{error}</Text> : null}
        <Animated.View style={[styles.moodContainer, { opacity: fadeAnim }]}>
          {moods.length > 0 ? (
            moods.map((mood, index) => (
              <TouchableOpacity key={index} style={styles.moodButton}>
                <Text style={styles.moodButtonText}>{mood}</Text>
              </TouchableOpacity>
            ))
          ) : (
            <Text style={styles.noMoodsText}>No moods predicted</Text>
          )}
        </Animated.View>
      </ScrollView>
      <View style={styles.navbar}>
        <TouchableOpacity style={styles.navItem}>
          <Feather name="home" color="#3498db" size={24} style={styles.navIcon} />
          <Text style={styles.navText}>Home</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Feather name="music" color="#3498db" size={24} style={styles.navIcon} />
          <Text style={styles.navText}>Lyrics</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Feather name="heart" color="#3498db" size={24} style={styles.navIcon} />
          <Text style={styles.navText}>Favorites</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Feather name="settings" color="#3498db" size={24} style={styles.navIcon} />
          <Text style={styles.navText}>Settings</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#f0f0f5',
  },
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    padding: 20,
    paddingBottom: 80, // Add padding to account for navbar
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#2c3e50',
    textAlign: 'center',
    marginBottom: 30,
  },
  textInput: {
    height: 150,
    borderColor: '#bdc3c7',
    borderWidth: 1,
    borderRadius: 12,
    marginBottom: 20,
    paddingHorizontal: 15,
    paddingVertical: 10,
    backgroundColor: '#fff',
    fontSize: 16,
    color: '#34495e',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 5,
  },
  button: {
    backgroundColor: '#3498db',
    borderRadius: 12,
    paddingVertical: 15,
    paddingHorizontal: 20,
    alignItems: 'center',
    marginBottom: 20,
    elevation: 4,
    shadowColor: '#2980b9',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  errorText: {
    color: '#e74c3c',
    textAlign: 'center',
    marginBottom: 10,
  },
  moodContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    marginTop: 20,
  },
  moodButton: {
    backgroundColor: '#2ecc71',
    borderRadius: 20,
    paddingVertical: 10,
    paddingHorizontal: 20,
    margin: 5,
    elevation: 3,
    shadowColor: '#27ae60',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  moodButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  noMoodsText: {
    color: '#7f8c8d',
    fontSize: 16,
    textAlign: 'center',
  },
  navbar: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    backgroundColor: '#fff',
    paddingVertical: 10,
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    elevation: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  navItem: {
    alignItems: 'center',
  },
  navIcon: {
    marginBottom: 4,
    transform: [{ scale: 1.2 }],
  },
  navText: {
    fontSize: 12,
    color: '#3498db',
  },
    
  
});

export default App;
