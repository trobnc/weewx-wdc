import React, { FunctionComponent } from "react";
import { ResponsiveCalendar } from "@nivo/calendar";
import moment from "moment";
import { NumberValue, scaleQuantize } from "d3-scale";
import { useMediaQuery } from "@react-hook/media-query";

import { ColorScale } from "@nivo/calendar";

import { CalendarDiagramBaseProps } from "./types";
import { TooltipCalendar } from "../components/tooltip-calendar";

export const CalendarDiagram: FunctionComponent<CalendarDiagramBaseProps> = (
  props: CalendarDiagramBaseProps
): React.ReactElement => {
  const small = useMediaQuery("(max-width: 672px)");
  const start = props.data[0].day;
  const end = props.data[props.data.length - 1].day;
  const yearDiff = moment(end).diff(start, "years");

  // @see https://nivo.rocks/storybook/?path=/story/calendarcanvas--custom-color-space-function
  // @see https://github.com/plouc/nivo/issues/744#issuecomment-573340879
  const color = (): ColorScale => {
    // @todo use https://github.com/d3/d3-scale#threshold-scales
    const defaultColorScale = scaleQuantize<string>()
      .domain([0, Math.max(...props.data.map((item) => item.value))])
      .range(props.color);

    const colorScale = (value: NumberValue) => {
      const number = parseFloat(String(value).replace(props.unit, "").trim());
      return defaultColorScale(number); //adding alpha channel
    };
    colorScale.ticks = (count: number | undefined) => {
      return defaultColorScale.ticks(count).map((e) => {
        console.log("e", e);
        return `${e}${props.unit}`;
      });
    };

    /*tslint-ignore*/
    return colorScale;
  };

  return (
    <>
      <p className="label">{props.heading}</p>
      <div
        className="calendar-diagram"
        // @todo Add responsive style.
        style={{ height: `${(yearDiff + 1) * (small ? 25 : 14)}vw` }}
      >
        <ResponsiveCalendar
          from={props.data[0].day}
          data={props.data}
          to={props.data[props.data.length - 1].day}
          emptyColor="#e0e0e0"
          //colors={props.color}
          colorScale={color()}
          margin={{
            top: 20,
            right: small ? 0 : 100,
            bottom: small ? 40 : 20,
            left: small ? 0 : 25,
          }}
          dayBorderColor="#ffffff"
          monthSpacing={2}
          monthBorderColor="#ffffff"
          monthLegendOffset={14}
          monthLegendPosition="after"
          yearSpacing={30}
          yearLegendOffset={10}
          tooltip={(data) => (
            <TooltipCalendar
              day={data.day}
              value={data.value}
              unit={props.unit}
              color={data.color}
            />
          )}
          legends={[
            {
              anchor: small ? "bottom-left" : "right",
              direction: small ? "row" : "column",
              translateY: small ? -20 : 0,
              translateX: small ? 0 : -20,
              itemCount: 4,
              itemWidth: small ? 50 : 80,
              itemHeight: 20,
              itemsSpacing: small ? 2 : 5,
              itemDirection: "left-to-right",
            },
          ]}
        />
      </div>
    </>
  );
};
