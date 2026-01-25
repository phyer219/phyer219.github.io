---
title: Interested talk on SCA/HPCAsia2026
date: 2026-01-25
category: physics
tags:
  - conference
---

This is a note for the interested talks: <https://www.sca-hpcasia2026.jp/index.html>

- [Monday, January 26](#monday-january-26)
  - [Tutorial 09:30 - 12:30 Room 1008](#tutorial-0930---1230-room-1008)
  - [13:30 - 16:30 • Tutorial](#1330---1630--tutorial)
- [Thursday, January 29](#thursday-january-29)
  - [11:30 - 12:30 Room 802](#1130---1230-room-802)
  - [12:30 - 13:30 12F Conference Hall](#1230---1330-12f-conference-hall)
  - [13:30 - 17:00 Room 1009](#1330---1700-room-1009)

## Monday, January 26

### Tutorial 09:30 - 12:30 Room 1008

Integrating distributed classical and quantum computing resources for hybrid workflows in the

Contributors: Sebastian Stern, Tyler Takeshita, and Benchen Huang

Abstract: Classical Quantum Monte Carlo (QMC) methods leverage high-performance computing (HPC) resources to simulate complex quantum many-body systems. Recently, these methods have been extended to quantum computers (QC) in hopes to achieve better accuracy. At the same time, architectures are being developed that enable such hybrid workflows by integrating quantum and HPC resources often hosted at different locations.

In this tutorial, we demonstrate a solution to an exemplary quantum many-body problem integrating distributed classical and quantum computing systems in the cloud. Specifically, we build an end-to-end workflow to execute the subroutines of a QMC algorithm on cloud-based batch and quantum computing resources and estimate the ground state energy of the example problem Hamiltonian.

The tutorial introduces QMC and QC basics to the participants and enables them to utilize cloud-native HPC and QC technologies for hybrid workloads. During the tutorial, participants will get free access to temporary AWS accounts and can follow along the guided steps in the QMC workflow. All attendees leave with code examples they can use as a foundation for their own projects.

### 13:30 - 16:30 • Tutorial

Workload and workflow management in quantum-classical HPC Room 1007

Mon, January 26, 2026 13:30 - 16:30 Room 1007

Contributors: Munetaka Ohtani, Shweta Salaria, and Yoonho Park

Abstract: Quantum computing has the potential to elevate heterogeneous high-performance computers to tackle

+

problems that are intractable for purely classical supercomputers. Integrating quantum processing units (QPUs) into a heterogeneous compute infrastructure, referred to as the quantum-centric supercomputing (QCSC) model, involves CPUs, GPUs, and other specialized accelerators (AlUs, etc.). Achieving this requires collaboration across multiple industries to align efforts in integrating hardware and software.

IBM and our HPC/Quantum partners have developed software components to enable the handling of QPU workloads within the Slurm workload manager in HPC environments. This tutorial session will provide a comprehensive overview of the architecture, demonstrate how to create Slurm jobs for executing quantum workloads, and discuss the execution of Quantum-Classical hybrid workloads. Participants will gain hands-on experience though live demonstrations, exploring the integration of quantum workloads into existing HPC systems.

Efficient scheduling is only part of the solution. In the second half of the session, we will address the orchestration challenges unique to hybrid Quantum-Classical workloads-such as iterative execution, hyperparameter tuning, and backend instability. Participants will learn how to build scalable, fault-tolerant pipelines using Python-based workflow tools like Prefect. Key features such as checkpointing, automatic retries, and real-time observability will be demonstrated live, equipping attendees with the skills to manage complex quantum workloads and prepare for future challenges in scalability and reproducibility.

## Thursday, January 29

### 11:30 - 12:30 Room 802

Birds of a Feather

New Software Ecosystem of Al for Science - Challenges and Opportunities

Contributors: Keita Teranishi, Brian van Essen

### 12:30 - 13:30 12F Conference Hall

• Lunch Speaker Session by Google Cloud Japan G.K.

Title: Accelerating Research and Discovery with Google Cloud GPUs: Featuring SyntheticGestalt's AI Workloads

Speaker 1: Kei Hoshino, Google Cloud, Customer Engineer

Speaker 2: Kotaro Kamiya, SyntheticGestalt, CTO

### 13:30 - 17:00 Room 1009

Tutorial

Performant and scalable simulation of open quantum systems

Contributors: Tyler Takeshita, Sebastian Stern, Benchen Huang, and Jin-Sung Kim

Abstract: Real-world quantum systems are subject to external interactions, no matter these interactions being intentional or unintentional. Efficient and accurate numerical simulation of open quantum systems (OQS), therefore, provide valuable insights into fundamental quantum processes responsible for experimental observations. Accurate simulations of OQSs are a crucial tool in designing higher performance quantum processors, enabling researchers to explore and optimize the vast parameter space of quantum hardware, uncover fundamental physics enabling higher performance qubits, and design higher fidelity control and readout methods. However, the computational demand of these simulations grows rapidly due to the exponentially increasing dimensionality of the Hilbert space and can require the use of high-performance compute (HPC) environments. In this tutorial, we demonstrate how to develop, test, and scale the simulations of OQS on AWS using CUDA-Q Dynamics and QuTiP, both accelerated by cuQuantum. The tutorial introduces open quantum dynamics basics and their computational considerations, independent of the underlying cloud architecture. During hands-on labs, we then architect cloud-native HPC solutions capable of leveraging accelerated compute resources, like Amazon EC2 P6 instances powered by NVIDIA Blackwell GPUs. Participants will get free access to temporary AWS accounts so they can provision their own HPC cluster during the tutorial. All attendees leave with code examples they can use as a foundation for their own projects.
