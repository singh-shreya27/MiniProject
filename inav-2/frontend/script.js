// document.addEventListener("DOMContentLoaded", () => {
//     const roomList = [
//         // Ground Floor
// "11ACG002", "11ACG004", "11ACG010", "11ACG008", "11ACG009", "11ACG006", "11ACG005", "11ACG013", 
// "11ACG012", "f0lift1", "f0lift2", "f0lift3", "f0lift4", "f0stair1", "f0stair2", "f0stair3", "f0stair4", 
// "f0stair5", "f0stair6",


// // 1st Floor
// "11AC1002", "11AC1015", "11AC1016", "11AC1017", "11AC1007", "11AC1005", "11AC1006", "11AC1019", 
// "11AC1020", "11AC1018", "11AC1010", "11AC1012", "11AC1008", "11AC1026", "11AC1025", "11AC1023", 
// "11AC1011", "11AC1024", "11AC1022", "11AC1009", "11AC1021", "11AC1004", "11AC1003", "11AC1013", 
// "f1lift1", "f1lift2", "f1lift3", "f1lift4", "f1stair1", "f1stair2", "f1stair3", "f1stair4",

// // 2nd Floor
// "11AC2004", "11AC2005", "11AC2003", "11AC2028", "11AC2044", "11AC2035", "11AC2038", "11AC2010", 
// "11AC2012", "11AC2019", "11AC2020", "11AC2021", "11AC2026", "11AC2027", "11AC2043", "11AC2013", 
// "11AC2014", "11AC2009", "11AC2011", "11AC2042", "11AC2007", "11AC2040", "11AC2039", "11AC2041", 
// "11AC2031", "11AC2008", "11AC2006", "11AC2016", "11AC2034", "11AC2033", "11AC2036", "11AC2037", 
// "11AC2022", "11AC2023", "11AC2024", "11AC2025", "f2lift1", "f2lift2", "f2lift3", "f2lift4", "f2lift5", 
// "f2lift6", "f2lift7", "f2lift8", "f2stair1", "f2stair2", "f2stair3", "f2stair4", "f2stair5", "f2stair6", 
// "f2stair7", "f2stair8", "f2stair9", "f2stair10",

// // 3rd Floor
// "11AC3021", "11AC3022", "11AC3023", "11AC3020", "11AC3019", "11AC3024", "11AC3025", "11AC3026", 
// "11AC3031", "11AC3032", "11AC3033", "11AC3034", "11AC3035", "11AC3036", "11AC3037", "11AC3038", 
// "11AC3027", "11AC3028", "11AC3029", "11AC3030", "11AC3042", "11AC3041", "11AC3040", "11AC3044", 
// "11AC3043", "11AC3046", "11AC3047", "11AC3045", "11AC3048", "11AC3014", "11AC3013", "11AC3009", 
// "11AC3011", "11AC3012", "11AC3010", "11AC3050", "11AC3049", "11AC3051", "11AC3054", "11AC3056", 
// "11AC3003", "11AC3002", "11AC3001", "11AC3055", "11AC3004", "11AC3005", "11AC3053", "11AC3052", 
// "11AC3007", "11AC3008", "11AC3006", "11AC3016", "11AC3017", "11AC3015", "f3lift1", "f3lift2", 
// "f3lift3", "f3lift4", "f3lift5", "f3lift6", "f3lift7", "f3lift8", "f3stair1", "f3stair2", "f3stair3", 
// "f3stair4",

// // 4th Floor
// "11AC4020", "11AC4021", "11AC4023", "11AC4022", "11AC4019", "11AC4015", "11AC4010", "11AC4014", 
// "11AC4013", "11AC4009", "11AC4011", "11AC4012", "11AC4006", "11AC4007", "11AC4008", "11AC4003", 
// "11AC4002", "11AC4001", "11AC4005", "11AC4004", "11AC4016", "11AC4028", "11AC4027", "11AC4030", 
// "11AC4029", "11AC4034", "11AC4031", "11AC4032", "11AC4033", "11AC4036", "11AC4035", "11AC4037", 
// "11AC4038", "11AC4039", "11AC4040", "11AC4042", "11AC4041", "11AC4018", "11AC4025", "f4lift1", 
// "f4lift2", "f4lift3", "f4lift4", "f4lift5", "f4lift6", "f4lift7", "f4lift8", "f4stair1", "f4stair2", 
// "f4stair3", "f4stair4"

//    ];
   

//     const splash = document.getElementById("splash");
//     const mobileFrame = document.getElementById("mobile-frame");
//     const startBtn = document.getElementById("startBtn");
//     const dropdownSection = document.getElementById("location-container");

//     const bubblesContainer = document.getElementById("bubbles-container");
//     const currentSearch = document.getElementById("current-search");
//     const destinationSearch = document.getElementById("destination-search");
//     const currentRoom = document.getElementById("current-room");
//     const destinationRoom = document.getElementById("destination-room");
//     const startNavigationBtn = document.getElementById("startNavigationBtn");

//     // Autocomplete setup
//     function setupAutocomplete(inputElement, dropdownElement) {
//         inputElement.addEventListener("input", () => {
//             const query = inputElement.value.trim().toLowerCase();
//             dropdownElement.innerHTML = "";

//             if (query.length === 0) {
//                 dropdownElement.style.display = "none";
//                 return;
//             }

//             const filtered = roomList.filter(room => room.toLowerCase().includes(query));

//             if (filtered.length === 0) {
//                 dropdownElement.style.display = "none";
//                 return;
//             }

//             filtered.forEach(room => {
//                 const li = document.createElement("li");
//                 li.textContent = room;
//                 li.addEventListener("click", () => {
//                     inputElement.value = room;
//                     dropdownElement.style.display = "none";
//                     inputElement.focus();
//                 });
//                 dropdownElement.appendChild(li);
//             });

//             dropdownElement.style.display = "block";
//         });





 document.addEventListener("DOMContentLoaded", () => {

    const roomList = [ 
                // Ground Floor
"11ACG002", "11ACG004", "11ACG010", "11ACG008", "11ACG009", "11ACG006", "11ACG005", "11ACG013", 
"11ACG012", "f0lift1", "f0lift2", "f0lift3", "f0lift4", "f0stair1", "f0stair2", "f0stair3", "f0stair4", 
"f0stair5", "f0stair6",


// 1st Floor
"11AC1002", "11AC1015", "11AC1016", "11AC1017", "11AC1007", "11AC1005", "11AC1006", "11AC1019", 
"11AC1020", "11AC1018", "11AC1010", "11AC1012", "11AC1008", "11AC1026", "11AC1025", "11AC1023", 
"11AC1011", "11AC1024", "11AC1022", "11AC1009", "11AC1021", "11AC1004", "11AC1003", "11AC1013", 
"f1lift1", "f1lift2", "f1lift3", "f1lift4", "f1stair1", "f1stair2", "f1stair3", "f1stair4",

// 2nd Floor
"11AC2004", "11AC2005", "11AC2003", "11AC2028", "11AC2044", "11AC2035", "11AC2038", "11AC2010", 
"11AC2012", "11AC2019", "11AC2020", "11AC2021", "11AC2026", "11AC2027", "11AC2043", "11AC2013", 
"11AC2014", "11AC2009", "11AC2011", "11AC2042", "11AC2007", "11AC2040", "11AC2039", "11AC2041", 
"11AC2031", "11AC2008", "11AC2006", "11AC2016", "11AC2034", "11AC2033", "11AC2036", "11AC2037", 
"11AC2022", "11AC2023", "11AC2024", "11AC2025", "f2lift1", "f2lift2", "f2lift3", "f2lift4", "f2lift5", 
"f2lift6", "f2lift7", "f2lift8", "f2stair1", "f2stair2", "f2stair3", "f2stair4", "f2stair5", "f2stair6", 
"f2stair7", "f2stair8", "f2stair9", "f2stair10",

// 3rd Floor
"11AC3021", "11AC3022", "11AC3023", "11AC3020", "11AC3019", "11AC3024", "11AC3025", "11AC3026", 
"11AC3031", "11AC3032", "11AC3033", "11AC3034", "11AC3035", "11AC3036", "11AC3037", "11AC3038", 
"11AC3027", "11AC3028", "11AC3029", "11AC3030", "11AC3042", "11AC3041", "11AC3040", "11AC3044", 
"11AC3043", "11AC3046", "11AC3047", "11AC3045", "11AC3048", "11AC3014", "11AC3013", "11AC3009", 
"11AC3011", "11AC3012", "11AC3010", "11AC3050", "11AC3049", "11AC3051", "11AC3054", "11AC3056", 
"11AC3003", "11AC3002", "11AC3001", "11AC3055", "11AC3004", "11AC3005", "11AC3053", "11AC3052", 
"11AC3007", "11AC3008", "11AC3006", "11AC3016", "11AC3017", "11AC3015", "f3lift1", "f3lift2", 
"f3lift3", "f3lift4", "f3lift5", "f3lift6", "f3lift7", "f3lift8", "f3stair1", "f3stair2", "f3stair3", 
"f3stair4",

// 4th Floor
"11AC4020", "11AC4021", "11AC4023", "11AC4022", "11AC4019", "11AC4015", "11AC4010", "11AC4014", 
"11AC4013", "11AC4009", "11AC4011", "11AC4012", "11AC4006", "11AC4007", "11AC4008", "11AC4003", 
"11AC4002", "11AC4001", "11AC4005", "11AC4004", "11AC4016", "11AC4028", "11AC4027", "11AC4030", 
"11AC4029", "11AC4034", "11AC4031", "11AC4032", "11AC4033", "11AC4036", "11AC4035", "11AC4037", 
"11AC4038", "11AC4039", "11AC4040", "11AC4042", "11AC4041", "11AC4018", "11AC4025", "f4lift1", 
"f4lift2", "f4lift3", "f4lift4", "f4lift5", "f4lift6", "f4lift7", "f4lift8", "f4stair1", "f4stair2", 
"f4stair3", "f4stair4"
    ];

    const currentSearch = document.getElementById("current-search");
    const destinationSearch = document.getElementById("destination-search");
    const currentRoom = document.getElementById("current-room");
    const destinationRoom = document.getElementById("destination-room");
    const startNavigationBtn = document.getElementById("startNavigationBtn");
    const resultBox = document.getElementById("result");

    function setupAutocomplete(inputElement, dropdownElement) {
        inputElement.addEventListener("input", () => {
            const query = inputElement.value.trim().toLowerCase();
            dropdownElement.innerHTML = "";

            if (!query) {
                dropdownElement.style.display = "none";
                return;
            }

            const filtered = roomList.filter(r =>
                r.toLowerCase().includes(query)
            );

            filtered.forEach(room => {
                const li = document.createElement("li");
                li.textContent = room;
                li.onclick = () => {
                    inputElement.value = room;
                    dropdownElement.style.display = "none";
                };
                dropdownElement.appendChild(li);
            });

            dropdownElement.style.display = filtered.length ? "block" : "none";
        });
    }

    setupAutocomplete(currentSearch, currentRoom);
    setupAutocomplete(destinationSearch, destinationRoom);

    startNavigationBtn.addEventListener("click", () => {
        const source = currentSearch.value.trim().toUpperCase();
        const destination = destinationSearch.value.trim().toUpperCase();

        if (!source || !destination) {
            alert("Please select both rooms.");
            return;
        }

        fetch(`/shortest-path?start=${source}&end=${destination}`)
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    resultBox.innerText =
                        data.path.join(" → ") +
                        "\nTime: " + data.time + " seconds";
                }
            })
            .catch(err => {
                console.error(err);
                alert("Backend not responding");
            });
    });

});






























    //     document.addEventListener("click", (event) => {
    //         if (!dropdownElement.contains(event.target) && event.target !== inputElement) {
    //             dropdownElement.style.display = "none";
    //         }
    //     });
    // }

    // setupAutocomplete(currentSearch, currentRoom);
    // setupAutocomplete(destinationSearch, destinationRoom);

    // // Splash screen logic
    // setTimeout(() => {
    //     splash.style.display = "none";
    //     if (mobileFrame) mobileFrame.style.display = "flex";
    // }, 6000);

    // // Create animated bubbles
    // const createBubbles = (count = 5) => {
    //     for (let i = 0; i < count; i++) {
    //         const bubble = document.createElement("div");
    //         bubble.className = "bubble";
    //         bubble.style.top = `${Math.random() * 100}vh`;
    //         bubble.style.left = `${Math.random() * 100}vw`;
    //         bubblesContainer.appendChild(bubble);
    //     }
    // };
    // createBubbles();

    // // Show dropdowns based on search input
    // currentSearch.addEventListener("input", () => {
    //     currentRoom.style.display = currentSearch.value.length > 0 ? "block" : "none";
    // });

    // destinationSearch.addEventListener("input", () => {
    //     destinationRoom.style.display = destinationSearch.value.length > 0 ? "block" : "none";
    // });

























    // Start navigation button logic (updated to hit backend on localhost:5000)
//     startNavigationBtn.addEventListener("click", () => {
//         const source = currentSearch.value.trim();
//         const destination = destinationSearch.value.trim();

//         if (!source || !destination) {
//             alert("Please select both rooms before starting navigation.");
//             return;
//         }

//         // fetch("http://localhost:5000/compute", {
//         //     method: "POST",
//         //     headers: {
//         //         "Content-Type": "application/json",
//         //     },
//         //     body: JSON.stringify({ source, destination }),
//         // })
//         // .then(response => response.blob())
//         // .then(blob => {
//         //     // Optionally handle blob (e.g., open image or download ZIP)
//         //     console.log("Navigation ZIP received.");
//         //     const url = window.URL.createObjectURL(blob);
//         //     const a = document.createElement("a");
//         //     a.href = url;
//         //     a.download = "navigation.zip";
//         //     a.click();
//         //     window.URL.revokeObjectURL(url);
//         // })
//         fetch(`/shortest-path?start=${source}&end=${destination}`)
//   .then(res => res.json())
//   .then(data => {
//     if (data.error) {
//       alert(data.error);
//     } else {
//       document.getElementById("result").innerText =
//         data.path.join(" → ") + "\nTime: " + data.time + " seconds";
//     }
//   })
//   .catch(err => {
//     console.error("Fetch error:", err);
//     alert("Something went wrong while fetching the result.");
//   });

//     //     .catch(error => {
//     //         console.error("Error starting navigation:", error);
//     //     });
//     // });

//     // Shortest path form handler (if you have another form)
//     const pathForm = document.getElementById("pathForm");
//     if (pathForm) {
//         pathForm.addEventListener("submit", function (e) {
//             e.preventDefault();
//             const start = document.getElementById("start").value;
//             const end = document.getElementById("end").value;

//             // fetch(`/shortest-path?start=${start}&end=${end}`)
//             //     .then(res => res.json())
//             //     .then(data => {
//             //         console.log("Shortest path:", data);
//             //     })
//             fetch(`/shortest-path?start=${start}&end=${end}`)
//   .then(res => res.json())
//   .then(data => {
//     if (data.error) {
//       alert(data.error);
//     } else {
//       document.getElementById("result").innerText =
//         data.path.join(" → ") + "\nTime: " + data.time;
//     }
//   })

//                 .catch(err => {
//                     console.error("Path fetch error:", err);
//                 });
//         });
//     }
// });

