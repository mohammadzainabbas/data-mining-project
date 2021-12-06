### Data Mining Project 👨🏻‍💻

</br>

<div>
  <a href="https://open.vscode.dev/mohammadzainabbas/data-mining-project" target="_blank" style="cursor: pointer;"> 
    <img src="https://open.vscode.dev/badges/open-in-vscode.svg" style="cursor: pointer;"/>
  </a>
</div>

### Table of contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
  * [About the Data](#about-the-data)

---

<a id="introduction" />

#### 1. Introduction

Since, during our stay in Brussels, we were a regular user of [`STIB-MIVB`](https://www.stib-mivb.be/) - Brussels' Public Transport Company. Like most of the companies nowadays, `STIB-MIVB` provide real-time GIS data for all the buses, trams and trains in Brussels. We will be working on few days worth of data pulled from [open data portal](https://opendata.stib-mivb.be/store/).

---

<a id="project-overview" />

#### 2. Project Overview

The aim of this project is to analyse the data and provide the following insights:

- [x] Analyze the vehicle speed over the different network segments, how it varies across segments and over time. Present this in a suitable visual
- [x] Analyze the vehicle delays at the different stops, how it varies across stops, and over time. Present this in a suitable visual way
- [x] Given a vehicle start time, do arrival time forecasting at a given stop in
the route of this vehicle. You should be able to test the accuracy of your forecasting by randomly splitting the given dataset in disjoint training and testing subsets.
- [x] The GPS tracks are for real people moving in Brussels. In fact they are from _Mahmoud_ and _Jean-Philippe_. You are asked to infer the mode of transport of each of these tracks (bus, tram, etc)
- [x] Think your own of a valuable analysis on this data

---

<a id="about-the-data" />

##### 2.1. About the Data

Before working on the project, let's explore what kind of data do we have. Professor collected about 3 weeks of data which consist of the following:

1. The location of all vehicles every +/- 30 seconds (in JSON format)
2. ESRI Shape files describing the map (lines and stops) of `STIB-MIVB` network, two snapshots `3 Sept, 2021` and `23 Sept, 2021`
3. GTFS files containing the offline plan/schedule covering the same period of the vehicle location data, two snapshots `3 Sept, 2021` and `23 Sept, 2021`
4. GPS tracks to identify the mode of transportation.

---
