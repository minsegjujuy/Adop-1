import React, { useState } from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  useMapEvents,
} from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "./react-leaflet.scss";
import { MarkerIcon } from "./react-leaflet-icon.js";

export const MapView = (props) => {
  //  const [position,setposition]=useState({ lat:  -24.09804180450979, lng:-65.07202148437501 })
  const { position, setposition, comando } = props;
  const [showPosition, setShowPosition] = useState(false);
  const [address, setAddress] = useState(null);
  function MyComponent() {
    const map = useMapEvents({
      click: (e) => {
        setposition(e.latlng);
        // L.marker([lat, lng], { icon }).addTo(map);
        //     const geocoder = L.control.geocoder.nomitatim();
        //   geocoder.reverse(
        //     e.latlng,
        //     map.options.crs.scale(map.getZoom()),
        //     (results) => {
        //       setAddress(results[0].name);
        //     }
        //   );
      },
    });
    return null;
  }

  const handleMarkerMouseOver = () => {
    setShowPosition(true);
  };

  const handleMarkerMouseOut = () => {
    setShowPosition(false);
  };

  return (
    <MapContainer center={position} zoom={13}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {!comando && (
        <Marker position={position} icon={MarkerIcon} draggable>
          <Popup>
            {address}{" "}
            {`Latitud: ${position.lat.toFixed(
              4
            )}, Longitud: ${position.lng.toFixed(4)}`}
          </Popup>
        </Marker>
      )}
      {comando === true && (
        <Marker position={position} icon={MarkerIcon}>
          <Popup>
            {address} {`Latitud: ${position.lat}, Longitud: ${position.lng}`}
          </Popup>
        </Marker>
      )}
      <MyComponent />
    </MapContainer>
  );
};
